import csv
import json
import pandas as pd
import numpy as np
from util.fileio import FileIo
import os.path

def read(file_in,file_out,sum,data_dic):
    
    content = pd.read_csv(file_in,compression='gzip')
    content = np.array(content)
    data_list = []
    
    time_line = []
    for line in content:   
        time_s = line[0]
        time_line.append(time_s)
        time_s = int(time_s)
        time_o = line[1]
        cpu = line[5]
        memory = line[6]
        order = [int(time_s//10e5), int((time_o-time_s)//10e5), round(cpu*100,2),round(memory*1000,0)]
        #print(order)
        if time_s not in data_dic:
            data_dic[time_s] = 1
        else:
            if data_dic[time_s] <= 100:
                if 5 <= order[1] <= 50 :
                    data_list.append(order)
                    sum += 1
                    data_dic[time_s] += 1
        
    print("The earliest: " + str(min(time_line)))
    print("The latest: " +str(max(time_line)))
    FileIo(file_out).twoListToFile(data_list,'a')
    return sum

def filtrate(file_in,file_out):
    lines = []
    try:
        FileIo(file_in).readAllLines(lines)
    except:
        return
    datas = []
    for line in lines:
        if int(line[1]) >= 1 and float(line[2]) >= 0.01 and int(line[3]) >=1:
            line = [int(line[0]),int(line[1]),line[2],int(line[3])]
            datas.append(line)
    datas = sorted(datas,key=lambda x:x[0],reverse=False)
    FileIo(file_out).twoListToFile(datas,'a')


def analyze(file_in):
    lines = []
    FileIo(file_in).readAllLines(lines)
    print(lines)
    times = []
    length = []
    for i in lines:
        times.append(lines[0])
        length.append(lines[1])
    print("range of times: ",end='')
    print(min(times),end="  ")
    print(max(times))
    for i in range(len(times)):
        if i > 1:
            if times[i] < times[i-1]:
                print("error")
    print("distribution of length: ", end='')
    print(np.mean(length))
def reform(file_in,file_out):
    lines = []
    with open(file_in,"r", errors= 'ignore') as object:
        for line in object:
            try:
                this_line = [float(value) for value in line.rstrip().split(',')]
                lines.append(this_line)
                FileIo(file_out).listToFile(this_line,'a')
            except:
                continue
    file_out2 = "/Volumes/DEV/processed/500(0).txt"
    lines = sorted(lines,key=lambda x:x[0],reverse=False)
    FileIo(file_out2).twoListToFile(lines,'w')

def renew(file_in,file_out):
    lines = []
    FileIo(file_in).readAllLines(lines)
    
    datas = []
    for line in lines:
        if  0.01<=float(line[2]) <= 1  :
            datas.append(line)
    datas = sorted(datas,key=lambda x:x[0],reverse=False)
    FileIo(file_out).twoListToFile(datas,'a')


            
        
        

if __name__ == "__main__":
    file_path = "/Volumes/DEV/task_usage/part-00000-of-00500.csv.gz"
    file_out = "/Volumes/DEV/processed/read(-1).txt"
    file_path3 = "/Volumes/DEV/processed/google.txt"
    #file_in = "/Volumes/DEV/processed/500.txt"
    #file_in2 = "/Volumes/DEV/processed/500(1).txt"
    #file_out = "/Volumes/DEV/processed/500(2).txt"
    total = 500
    sum0 = 0
    sum = 0
    data_dic = {}
    assert not os.path.isfile(file_out)
    for one in range(total):
        print(one)
        path = file_path
        time = str(one).zfill(5)
        path = path.replace("00000",time)
        sum = read(file_path,file_out,sum,data_dic)
        if sum > sum0 :
            print("Difference : " +str(sum - sum0))
            sum0 = sum
        else:
            break
    
        #filtrate(file_out,file_out2)
    
    #reform(file_in,file_out)
    renew(file_out,file_path3)





