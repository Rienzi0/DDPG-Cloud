from cProfile import label
import numpy as np
import time
import matplotlib
from matplotlib import pyplot as plt
from core.machine import Machine
from core.task import Task
from core.cluster import Cluster
from util.fileio import FileIo
from ddpg.DDPG_model_large import DDPG
import random
from base_utilize import *

textname = "50"
#filepath_input = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/create/create_tasks_" + str(textname) + ".txt"
#filepath_input = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/real/real_tasks_300"  + "_2.txt"

def draw(file_path,pic_out):#任务数量
    all_batch_tasks = FileIo(file_path).readAllBatchLines()
    tnum_list = []
    len_list = []
    taskl_list = []
    step = 600
    for i,tasks in enumerate(all_batch_tasks):
        l = []
        for j in tasks:
            l.append(j[1])
            taskl_list.append(j[1])
        len_list.append(sum(l))
        tnum_list.append(len(tasks))
    #print(np.std(taskl_list))
    #print(np.mean(taskl_list))
    #print(tnum_list)
    num_list = []
    for i in range(len(len_list)):
        if i%step == 0:

            num_list.append(sum(tnum_list[i : i + 600]))
    #print(len(num_list))
    num_list = num_list[0:-1]

    t_list = range(0,len(num_list))

    fig,ax1=plt.subplots()
    ax1.plot(t_list,num_list,ls = '-',lw = 1, label = "tnum")
    name = "task number in every 10 mins"
    ax1.set_title(name)
    #ax1.legend()#
    #plt.show()
    plt.savefig(pic_out+"/"+name,dpi = 1000,format = "eps")

def draw_len(file_path,pic_out):
    all_batch_tasks = FileIo(file_path).readAllBatchLines()
    
    len_list = []
    
    step = 600
    for i,tasks in enumerate(all_batch_tasks):
        l = []
        for j in tasks:
            l.append(j[1])
        len_list.append(sum(l))
    step_len_list = []
    for i in range(len(len_list)):
        if i%step == 0:
            step_len_list.append(sum(len_list[i:i+step]))
    step_len_list = step_len_list[0:-1]
    t_list = range(0,len(step_len_list))
    fig,ax1=plt.subplots()
    ax1.plot(t_list,step_len_list,ls = '-',lw = 1, label = "tnum")
    name = "total task length in every 10 mins"
    ax1.set_title(name)
    #ax1.legend()#
    #plt.show()
    #plt.savefig(pic_out+"/"+name,dpi = 1000,format = "eps")
def draw_u(file_path,pic_out):
    all_batch_tasks = FileIo(file_path).readAllBatchLines()
    
    len_list = []
    
    step = 600
    for i,tasks in enumerate(all_batch_tasks):
        l = []
        for j in tasks:
            l.append(j[2])
        len_list.append(np.mean(l))
    step_u_list = []
    for i in range(len(len_list)):
        if i%step == 0:
            step_u_list.append(np.mean(len_list[i:i+step]))
    step_u_list = step_u_list[0:-1]
    t_list = range(0,len(step_u_list))
    fig,ax1=plt.subplots()
    ax1.plot(t_list,step_u_list,ls = '-',lw = 1, label = "tnum")
    name = "average cpu core utilization in every 10 mins"
    ax1.set_title(name)
    #ax1.legend()#
    plt.show()
    #plt.savefig(pic_out+"/"+name,dpi = 1000,format = "eps")
    
if __name__ == "__main__":
    filepath_input = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/real/real_tasks(5-200).txt"
    filepath_input = "/Users/rienzi/Desktop/实验代码/Pycloudsim/result/create_l_50.txt"
    #file_out = "/Users/rienzi/Desktop/drl/实验数据/low cluster 5-200(2)/pics"
    file_out = "/Users/rienzi/Desktop/drl/paper/pics/1"
    draw_len(filepath_input,file_out)
    #draw(filepath_input,file_out)
    #draw_u(filepath_input,file_out)