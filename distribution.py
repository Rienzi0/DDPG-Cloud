#analye the task distribution on VMs
from cProfile import label
import numpy as np
import math
from util.fileio import FileIo
from matplotlib import pyplot as plt



def main(file_input, file_output):
    # 读取结果数据，task feature
    result = []
    result = FileIo(file_input).readAllLines(result)

    #analyze_result = FileIo(file_output)
    
    
    di_list_l = [0 for i in range(20)]
    di_list_n = [0 for i in range(20)]
    di_list_s = [0 for i in range(20)]
    for task in result: #生成数据集：100-200 真实数据集：10-100
        key = int(task[1])
        if task[2] >= 200: 
            di_list_l[key] += 1
        elif task[2] <= 100:
            di_list_s[key] += 1 
        else:
            di_list_n[key] += 1
    color = [(217/255,208/255,190/255),(132/255,115/255,126/255),(245/255,192/255,141/255)]
    x = [str(i) for i in range(20)]
    plt.figure(figsize=(8,6))
    plt.bar(x,di_list_s,color=color[1],label = "short")
    plt.bar(x,di_list_n,color=color[0],bottom=di_list_s,label="normal")
    plt.bar(x,di_list_l,color=color[2],bottom=np.array(di_list_s)+np.array(di_list_n),label="long")
    plt.xlabel("VM ID",weight="bold")
    plt.ylabel("total task number",weight="bold")
    
    plt.legend()
    ax=plt.gca()
    ax.spines["bottom"].set_linewidth(2)
    ax.spines["top"].set_linewidth(2)
    ax.spines["left"].set_linewidth(2)
    ax.spines["right"].set_linewidth(2)
    plt.xticks(weight='bold')
    plt.yticks(weight='bold')
    plt.savefig(file_output+"/17.eps",dpi = 1000,format = "eps")
def draw1(file_input1,file_input2, file_output):
    result1 = []
    result1 = FileIo(file_input1).readAllLines(result1)
    result2 = []
    result2 = FileIo(file_input2).readAllLines(result2)

    di_list_l1 = [0 for i in range(20)]
    di_list_n1 = [0 for i in range(20)]
    di_list_s1 = [0 for i in range(20)]
    for task in result1: #生成数据集：100-200 真实数据集：10-100
        key = int(task[1])
        if task[2] >= 200: 
            di_list_l1[key] += 1
        elif task[2] <= 100:
            di_list_s1[key] += 1 
        else:
            di_list_n1[key] += 1

    di_list_l2 = [0 for i in range(20)]
    di_list_n2 = [0 for i in range(20)]
    di_list_s2 = [0 for i in range(20)]
    for task in result2: #生成数据集：100-200 真实数据集：10-100
        key = int(task[1])
        if task[2] >= 200: 
            di_list_l2[key] += 1
        elif task[2] <= 100:
            di_list_s2[key] += 1 
        else:
            di_list_n2[key] += 1
    color = [(217/255,208/255,190/255),(132/255,115/255,126/255),(245/255,192/255,141/255)]
    width = 0.5
    x = [str(i) for i in range(20)]
    x0 = [(i-width/2) for i in range(20)]

    plt.figure(figsize=(8,6))
    plt.bar(x0,di_list_s1,width=width,color=color[1],label = "short")
    plt.bar(x0,di_list_n1,width=width,color=color[0],bottom=di_list_s1,label="normal")
    plt.bar(x0,di_list_l1,width=width,color=color[2],bottom=np.array(di_list_s1)+np.array(di_list_n1),label="long")

    x1 = [(i+width/2) for i in range(20)]
    


    plt.bar(x1,di_list_s2,width=width,color=color[1],label = "short")
    plt.bar(x1,di_list_n2,width=width,color=color[0],bottom=di_list_s2,label="normal")
    plt.bar(x1,di_list_l2,width=width,color=color[2],bottom=np.array(di_list_s2)+np.array(di_list_n2),label="long")
    plt.xticks(x,labels=x)
    plt.xlabel("VM ID",weight="bold")
    plt.ylabel("total task number",weight="bold")
    
    plt.legend()
    ax=plt.gca()
    ax.spines["bottom"].set_linewidth(2)
    ax.spines["top"].set_linewidth(2)
    ax.spines["left"].set_linewidth(2)
    ax.spines["right"].set_linewidth(2)
    plt.xticks(weight='bold')
    plt.yticks(weight='bold')
    plt.show()
    #plt.savefig(file_output+"/17.eps",dpi = 1000,format = "eps")


if __name__ == '__main__':


    file_output = "/Users/rienzi/Desktop/drl/paper/pics"
    
    
    file_input1 = "result/create_l_50.txt"
    #file_input = "new_real/b=0.9(5-200).txt"
    #file_input = "result/dqn_real.txt"
    file_input2 = "result/dqn5-200.txt" #create
    #main(file_input, file_output)
    draw1(file_input1,file_input2,file_output)
