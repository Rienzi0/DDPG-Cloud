from ctypes import util
import pandas as pd
import numpy as np
from pandas import DataFrame
import pickle
from util.fileio import FileIo
import random
csv_path = '/Volumes/Aether/batch_instance.csv'
txt_path = '/Volumes/Aether/raw_data2.txt'
txt_path = '/Volumes/Aether/real_tasks2.txt'
file_out = '/Volumes/Aether/real_tasks3.txt'
#txt_path2 = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/real/real_tasks.txt"
#file_out2 = "/Users/rienzi/Desktop/实验代码/Pycloudsim/data/real/real_tasks2.txt"
#时间按秒，第一天数量极少（基本处于23小时之后），最高第八天
read_chunks = pd.read_csv(csv_path, encoding='utf-8', iterator=True, chunksize=65535)
# 第二种只读取某一段数据（65535个数据）
'''
base_df = read_chunks.get_chunk(65535)
data_array = np.array(base_df)
date_list = []
for i in data_array:
    date_list.append(i[5])
'''
#print(np.max(date_list))
#print(np.min(date_list))
#print(base_df.loc['0'])
#print(base_df)
'''
for index, row in base_df.iterrows():
    print(index)
    #print(row)
'''

#list(base_df.itertuples(index=False))

# 第一种读取所有的chunk块并将所有块拼接成一个DataFrame
#chunk_list = list()
def read_c(txt_path):
    datalist = []
    #time_l = [i for i in range(86400,172801)]
    #time_l = [i for i in range(172800,259201)]
    #time_l = [i for i in range(259200,345601)]
    #time_l = [i for i in range(345600,432001)]
    #time_l = [i for i in range(432000,518401)]
    #time_l = [i for i in range(518400,604801)]
    #time_l = [i for i in range(604800,691201)]
    time_l = [i for i in range(691200,777601)]
    data_dict = {}
    progress = 0
    for i in time_l:
        data_dict[i] = 0
    #FileIo(txt_path).dictToFile(data_dict,'w')
    #print(data_dict)
    for chunk in read_chunks:
        #print(chunk)
        chunk_data = np.array(chunk)
        for i in chunk_data:
            if i[5] >= 691200 and i[5] <=777600:
                t_len = i[6] - i[5]
                if t_len >=5 and t_len<=50:
                    #print(1)
                    #if i[10] <= 100:  cpu利用率限制
                    if data_dict[i[5]] < 100:      #限制同时提交的任务数量
                        order = [i[5],i[6],i[10],i[12]]
                        if order[2] >=0.01:
                            datalist.append(order)
                            data_dict[i[5]] += 1
                            progress += 1
        if sum(data_dict.values()) >= (259200 - 172800) * 100:
            break
        if progress%1000 == 0:
            print(progress)
        #chunk_list.append(chunk)
        # print(chunk, type(chunk))
    FileIo(txt_path).twoListToFile(datalist,'w')
    #print(data_dict)
        
def filtrate(txt_path,file_out):
    lines = []
    FileIo(txt_path).readAllLines(lines)
    tasks = []

    for line in lines:
        if line[2] >= 0.01 :
            
            line_2 = [int(line[0]),int(line[1]),round(line[2],2),round(line[3],1)]
            tasks.append(line_2)
    FileIo(file_out).twoListToFile(tasks,'w')
    print(len(tasks))

def product(txt_path,file_out):
    lines = []
    FileIo(txt_path).readAllLines(lines)
    tasks = []
    for line in lines:
        if str(line[2]) != 'nan' and str(line[3]) != 'nan':
            task = [float(line[0])-691200,float(line[1])-float(line[0]),float(line[2])/100,float(line[3])*100]
            task[0] = int(task[0])
            task[1] = int(task[1])
            task[2] = round(task[2],2)
            task[3] = int(task[3])
            tasks.append(task)

    tasks = sorted(tasks,key=lambda x:x[0],reverse=False)
    FileIo(file_out).twoListToFile(tasks,'w')
    #print(len(tasks))

if __name__ == "__main__":
    #csv_path = '/Volumes/Aether/batch_instance.csv'
    #txt_path = '/Volumes/Aether/raw_data2.txt'

    txt_path = '/Volumes/Aether/real_tasks(5-50)(day8)(-2).txt'
    file_out = '/Volumes/Aether/real_tasks(5-50)(day8)(-1).txt'
    file_out2 = '/Volumes/Aether/real_tasks(5-50)(day8).txt'
    read_c(txt_path)
    product(txt_path,file_out)
    filtrate(file_out,file_out2)