from core.cluster import Cluster
from core.machine import Machine
from core.task import Task
from util.fileio import FileIo
from core.scheduler import Earliest_scheduler
from core.scheduler import Random_scheduler
from core.scheduler import Round_robin_scheduler
from base_utilize import *


def example(cluster, scheduler, filepath_input, filepath_output):
    all_batch_tasks = FileIo(filepath_input).readAllBatchLines()

    # 调度器初始化
    if scheduler == "random":
        my_scheduler = Random_scheduler(len(cluster.machines))
    elif scheduler == "earliest":
        my_scheduler = Earliest_scheduler(len(cluster.machines))
    elif scheduler == "rr":
        my_scheduler = Round_robin_scheduler(len(cluster.machines))

    for batch_tasks in all_batch_tasks:
        tasks_list = []
        for task in batch_tasks:
            tasks_list.append(Task(task[0], task[1], task[2], task[3]))  # 构建任务

        if scheduler == "random":
            machines_id = my_scheduler.scheduler(len(tasks_list))
        elif scheduler == "earliest":
            machines_id = my_scheduler.scheduler_o(len(tasks_list), tasks_list[0].start_time, cluster.machines)
        elif scheduler == "rr":
            machines_id = my_scheduler.scheduler(len(tasks_list))
            

        cluster.submit_tasks(tasks_list, machines_id)  # 提交任务到集群，并调度到虚拟机进行计算

    finished_tasks = []
    for task in cluster.finished_tasks:
        finished_tasks.append(task.feature)
    FileIo(filepath_output).twoListToFile(finished_tasks, "w")


if __name__ == '__main__':
    scheduler_li = ["random", "earliest", "rr"]  # "random", "earliest", "rr"
    txtname = ["300"]  # "1", "3", "5", "7", "9", "300", "3000"
    cluster = create_big()
    for scheduler in scheduler_li:
        for name in txtname:
            #filepath_input = "data/create/create_tasks_l_50.txt"
            #filepath_input ="data/real/real_tasks(5-50)(100).txt"
            filepath_input = "data/real/google.txt"
            #filepath_input = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/create/create_tasks_long_50.txt"
            filepath_output = "/Users/rienzi/Desktop/实验代码/Pycloudsim/result/finished_tasks_" + scheduler + ".txt"
            example(cluster, scheduler, filepath_input, filepath_output)
            cluster.reboot()  # 结束之后重启，开始下一轮仿真
            print(scheduler + ":" + name)
