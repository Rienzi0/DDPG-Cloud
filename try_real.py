import numpy as np
import time

from core.machine import Machine
from core.task import Task
from core.cluster import Cluster
from util.fileio import FileIo
from ddpg.DDPG_model_v2 import DDPG
import random
from base_utilize import *

MULTI_DC = True  # 是否为多数据中心
alpha = 10  # 多数据中心，计算虚拟机权重时micost权重调节因子
beta = 0.1  # 多数据中心，计算虚拟机权重时speed权重调节因子
gamma = 0.005  # 多数据中心，计算奖励时成本的权重调节因子

taskDim = 3
vmDim = 3 if MULTI_DC else 2

wait_p = 1 #用于反馈一个任务是否经过了等待才开始执行
bbeta = 0.9
# 通过任务和机器获取状态
def get_state(tasks_list, machines, tasksNum):
    tasks_state = [0] * (taskDim * tasksNum + 6 ) #textname = 9 时，taskdim = 3， tasksnum = 11
    for i, task in enumerate(tasks_list):
        tasks_state[taskDim * i] = task.mi
        tasks_state[taskDim * i + 1] = task.cpu_utilization
        tasks_state[taskDim * i + 2] = task.data_size / machines[0].speed
    
    
    mi_list = [i.mi for i in tasks_list]
    cpu_list = [i.cpu_utilization for i in tasks_list]
    size_list = [i.data_size / machines[0].speed for i in tasks_list]
    # ablation
    #tasks_state[-6] = 0
    #tasks_state[-5] = 0
    #tasks_state[-4] = 0
    #tasks_state[-3] = 0
    #tasks_state[-2] = 0
    #tasks_state[-1] = 0
    #'''
    tasks_state[-6] = round(np.std(mi_list),2)
    tasks_state[-5] = round(np.std(cpu_list),2)
    tasks_state[-4] = round(np.std(size_list),2)

    
    co1 = np.corrcoef(mi_list,cpu_list)[0][1]
    co2 = np.corrcoef(cpu_list,size_list)[0][1]
    co3 = np.corrcoef(size_list,mi_list)[0][1]
    if str(co1) == 'nan':
        co1 = 0
    if str(co2) == 'nan':
        co2 = 0
    if str(co3) == 'nan':
        co3 = 0

    tasks_state[-3] = abs(co1)
    tasks_state[-2] = abs(co2)
    tasks_state[-1] = abs(co3)   #三个参量两两之间的pcc
    #'''
    #print(tasks_state[-1])
    start_time = tasks_list[0].start_time  # 当前批次任务的开始时间
    machines_state = []
    leisure_machines_id = []  # 存储空闲机器的id
    for machine in machines:
        machines_state.append(machine.mips)
        machines_state.append(max(machine.next_start_time - start_time, 0))  # 等待时间
        if MULTI_DC:
            #machines_state.append(machine.speed)
            machines_state.append(machine.micost)
        if machine.next_start_time <= start_time:  # 表示当前时刻机器空闲
            leisure_machines_id.append(machine.id)

    # 使用机器的mips作为概率权重，对所有机器采样
    if MULTI_DC:
        #machines_weight_value = [m.mips - alpha * m.micost + beta * m.speed for m in machines]
        machines_weight_value = [m.mips - alpha * m.micost  for m in machines]
    else:
        machines_weight_value = [m.mips for m in machines]
    machines_weight_pro = np.array([i / sum(machines_weight_value) for i in machines_weight_value])
    new_leisure_machines_id_first = np.random.choice([i for i in range(len(machines))], size=len(machines),
                                                     replace=True,
                                                     p=machines_weight_pro.ravel()).tolist()  # replace又放回取，size次数
    # 对空闲机器采样
    machines_weight_value = [machines[id].mips for id in leisure_machines_id]
    machines_weight_pro = np.array([i / sum(machines_weight_value) for i in machines_weight_value])
    if len(leisure_machines_id)!= 0:
        new_leisure_machines_id_second = np.random.choice(leisure_machines_id, size=len(leisure_machines_id),
                                                          replace=True,
                                                          p=machines_weight_pro.ravel()).tolist()  # replace又放回取，size次数
    else:
        new_leisure_machines_id_second = []

    leisure_machines_id += new_leisure_machines_id_first
    random.shuffle(leisure_machines_id)  # 打乱

    # 本实验中用0填充了一些无效动作，虚拟机编号从1开始，所以需要统一加1
    leisure_machines_id_plus = [i + 1 for i in leisure_machines_id]
    state = tasks_state + machines_state  #状态包括所有任务的状态和所有虚拟机的状态
    return state, leisure_machines_id_plus


def main(cluster, tasksNum, filepath_input, filepath_output):
    vmsNum = len(cluster.machines)
    all_batch_tasks = FileIo(filepath_input).readAllBatchLines()
    print("环境创建成功！")
    loss_set = []
    state_all = []  # 存储所有的状态 [None, tasksNum*taskDim+vmsNum*vmDim]
    action_all = []  # 存储所有的动作 [None, vmsNum]
    reward_all = []  # 存储所有的奖励 [None, 1]

    DRL = DDPG(tasksNum, taskDim, vmsNum, vmDim)
    print("网络初始化成功！")
    #exit()

    for step, batch_tasks in enumerate(all_batch_tasks):
        tasks_list = []
        for task in batch_tasks:
            tasks_list.append(Task(task[0], task[1], task[2], task[3]))  # 构建任务
            
        state, leisure_machines_id_plus = get_state(tasks_list, cluster.machines, tasksNum)
        state_all.append(state)

        machines_id_pluse = DRL.choose_action(np.array(state), len(tasks_list), leisure_machines_id_plus)  # 通过调度算法得到动作
        machines_id = (machines_id_pluse - 1).astype(int).tolist()
        cluster.submit_tasks(tasks_list, machines_id)  # 提交任务到集群，并调度到虚拟机进行计算
        action_all.append(machines_id_pluse)

        ###添加了task.wait_time 表示任务提交时，虚拟机中没执行完的任务总运行时间
        ###
        
        reward_p = 0
        for task in cluster.finished_tasks[-len(tasks_list):]:
            if task.wait_time != 0 :
                reward_p += wait_p / len(tasks_list)
            #print(task.task_cost)
        ''''''
        c_max = 0
        c_min = 100000
        r_max = 0
        r_min = 100000
        for task in cluster.finished_tasks[-len(tasks_list):]:
            if task.task_response_time / task.mi > r_max:
                r_max = task.task_response_time
            elif task.task_response_time / task.mi < r_min:
                r_min = task.task_response_time / task.mi
            if task.task_run_time * cluster.machines[task.task_machine_id].micost > c_max:
                c_max = task.task_run_time * cluster.machines[task.task_machine_id].micost
            elif task.task_run_time * cluster.machines[task.task_machine_id].micost < c_min:
                c_min = task.task_run_time * cluster.machines[task.task_machine_id].micost

        # for ablation
        '''
        reward = 10 * [ bbeta * (task.task_response_time / task.mi ) + (1 - bbeta) * (task.task_run_time * cluster.machines[task.task_machine_id].micost ) for task in cluster.finished_tasks[-len(tasks_list):]]
        '''
        reward = 10*[ bbeta * (task.task_response_time / task.mi - r_min)/(r_max - r_min) + (1 - bbeta) * (task.task_run_time * cluster.machines[task.task_machine_id].micost / c_max) for task in cluster.finished_tasks[-len(tasks_list):]]
        
        #print(reward_p)
        #print(sum(reward))

        # 便历刚刚提交的一批任务，记录动作和奖励
        #if MULTI_DC:
        #reward 为一个batch的reward
        
        #reward = [(task.task_response_time / task.mi + gamma * task.task_run_time * cluster.machines[task.task_machine_id].micost) for task in cluster.finished_tasks[-len(tasks_list):]]
        
        #r_s = sum(reward)
        reward_all.append([(sum(reward) + reward_p)/ len(reward)])
        #reward_all.append([(sum(reward) )/ len(reward)])
        # 减少存储数据量
        if len(state_all) > 6000:
            state_all = state_all[-3000:]
            action_all = action_all[-3000:]
            reward_all = reward_all[-3000:]

        # 先存储一些经验，再学习
        if (step > 400):
            # 截取最后1000条记录
            new_state = np.array(state_all, dtype=np.float32)[-3000:-1]
            new_action = np.array(action_all, dtype=np.float32)[-3000:-1]
            new_reward = np.array(reward_all, dtype=np.float32)[-3000:-1]

            DRL.store_memory(new_state, new_action, new_reward)
            DRL.step = step
            loss = DRL.learn()
            if (step % 1000 == 0):
                print("程序运行时间：%.8s s" % (time.time() - start_time))
                print("step:", step)
                print("loss:", loss)
                loss_set.append(float(loss))
                print("还有这么多步:", len(all_batch_tasks) - step)
                print()
        
        #if (step > 1000):  # test
           #break
    #DRL.writer.close()
    finished_tasks = []
    #print(loss_set)
    for task in cluster.finished_tasks:
        finished_tasks.append(task.feature)
    FileIo(filepath_output).twoListToFile(finished_tasks, "w")


if __name__ == '__main__':
    start_time = time.time()
    cluster = create_big()
    #txtname = [300]  # 1, 3, 5, 7, 9
    #for name in txtname:
    #filepath_input = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/real/real_tasks_" + str(name) + "_4.txt"  
    #filepath_input = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/create/create_tasks_long_50.txt"
    #filepath_input = "data/real/real_tasks(5-50)(100).txt"
    filepath_input = "data/real/google.txt"
    #filepath_input = "data/create/create_tasks_l_50.txt"
    print(filepath_input)
    #filepath_output = "new_real/b=0.9(5-50)(100).txt"
    filepath_output = "new_real/b=0.9(google).txt"
    print(filepath_output)
    tasksNum = 100# 每次提交的最大任务，创建数据时进行了限制
    main(cluster, tasksNum, filepath_input, filepath_output)
    cluster.reboot()  # 结束之后重启，开始下一轮仿真
    print("完成: " + filepath_output)
