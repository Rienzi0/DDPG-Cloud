from core.cluster import Cluster
from core.machine import Machine

# 创建集群
def creat_cluster():
    cluster = Cluster()
    for i in range(2):
        cluster.add_machine(Machine(mips=600, speed=450, micost=1))  # 构建虚拟机
    for i in range(2):
        cluster.add_machine(Machine(mips=500, speed=450, micost=1))
    for i in range(2):
        cluster.add_machine(Machine(mips=400, speed=450, micost=1))
    for i in range(2):
        cluster.add_machine(Machine(mips=300, speed=450, micost=1))
    for i in range(2):
        cluster.add_machine(Machine(mips=200, speed=450, micost=1))
    return cluster

# 创建大集群
def creat_cluster_large():
    cluster = Cluster()
    for i in range(5):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=1))  # 构建虚拟机
    for i in range(5):
        cluster.add_machine(Machine(mips=1000, speed=500, micost=1))
    for i in range(5):
        cluster.add_machine(Machine(mips=500, speed=500, micost=1))
    for i in range(5):
        cluster.add_machine(Machine(mips=250, speed=500, micost=1))
    return cluster

# 创建大集群
def creat_cluster_large_multiple():
    cluster = Cluster()
    for i in range(4):
        cluster.add_machine(Machine(mips=2000, speed=560, micost=1.71))  # 构建虚拟机
    for i in range(4):
        cluster.add_machine(Machine(mips=1500, speed=529, micost=2.23))
    for i in range(4):
        cluster.add_machine(Machine(mips=1000, speed=511, micost=2.3))
    for i in range(4):
        cluster.add_machine(Machine(mips=500, speed=448, micost=2.19))
    for i in range(4):
        cluster.add_machine(Machine(mips=250, speed=467, micost=2.18))
    return cluster


def creat_20_cluster():
    cluster = Cluster()
    for i in range(4):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=1.71))  # 构建虚拟机
    for i in range(4):
        cluster.add_machine(Machine(mips=1500, speed=500, micost=2.23))
    for i in range(4):
        cluster.add_machine(Machine(mips=1000, speed=500, micost=2.3))
    for i in range(4):
        cluster.add_machine(Machine(mips=500, speed=500, micost=2.19))
    for i in range(4):
        cluster.add_machine(Machine(mips=300, speed=500, micost=2.18))
    return cluster

def creat_40_cluster():
    cluster = Cluster()
    for i in range(4):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=1.71))  # 构建虚拟机
    for i in range(4):
        cluster.add_machine(Machine(mips=1700, speed=500, micost=1.75))
    for i in range(4):
        cluster.add_machine(Machine(mips=1500, speed=500, micost=2.23))
    for i in range(4):
        cluster.add_machine(Machine(mips=1200, speed=500, micost=2.02))
    for i in range(4):
        cluster.add_machine(Machine(mips=1000, speed=500, micost=1.97))
    for i in range(4):
        cluster.add_machine(Machine(mips=700, speed=500, micost=2.54))
    for i in range(4):
        cluster.add_machine(Machine(mips=600, speed=500, micost=2.19))
    for i in range(4):
        cluster.add_machine(Machine(mips=500, speed=500, micost=2.37))
    for i in range(4):
        cluster.add_machine(Machine(mips=400, speed=500, micost=2.3))
    for i in range(4):
        cluster.add_machine(Machine(mips=300, speed=500, micost=2.18))
    return cluster

def creat_10_cluster():
    cluster = Cluster()
    for i in range(2):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=1.71))  # 构建虚拟机
    for i in range(2):
        cluster.add_machine(Machine(mips=1500, speed=500, micost=2.23))
    for i in range(2):
        cluster.add_machine(Machine(mips=1000, speed=500, micost=2.3))
    for i in range(2):
        cluster.add_machine(Machine(mips=500, speed=500, micost=2.19))
    for i in range(2):
        cluster.add_machine(Machine(mips=250, speed=500, micost=2.18))
    return cluster

def creat_20_low():
    cluster = Cluster()
    for i in range(4):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=1.71))  # 构建虚拟机
    for i in range(4):
        cluster.add_machine(Machine(mips=1500, speed=500, micost=2.23))
    for i in range(4):
        cluster.add_machine(Machine(mips=500, speed=500, micost=2.3))
    for i in range(4):
        cluster.add_machine(Machine(mips=400, speed=500, micost=2.19))
    for i in range(4):
        cluster.add_machine(Machine(mips=300, speed=500, micost=2.18))
    return cluster


def creat_new():
    cluster = Cluster()
    for i in range(5):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=2.416))  # 构建虚拟机
    for i in range(5):
        cluster.add_machine(Machine(mips=1500, speed=500, micost=1.826))
    for i in range(5):
        cluster.add_machine(Machine(mips=500, speed=500, micost=0.648))
    for i in range(5):
        cluster.add_machine(Machine(mips=250, speed=500, micost=0.353))
    
    return cluster

def create_big():
    cluster = Cluster()
    for i in range(5):
        cluster.add_machine(Machine(mips=8000, speed=500, micost=8.637))
    #for i in range(5):
    #    cluster.add_machine(Machine(mips=4000, speed=500, micost=4.348))
    for i in range(5):
        cluster.add_machine(Machine(mips=3000, speed=500, micost=3.594))  # 构建虚拟机
    for i in range(5):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=2.416))
    for i in range(5):
        cluster.add_machine(Machine(mips=1500, speed=500, micost=1.826))
    #for i in range(5):
    #    cluster.add_machine(Machine(mips=1000, speed=500, micost=1.237))
    #for i in range(10):
    #    cluster.add_machine(Machine(mips=500, speed=500, micost=0.648))
    #for i in range(15):
    #    cluster.add_machine(Machine(mips=250, speed=500, micost=0.353))
    
    return cluster
'''
def create_big():
    cluster = Cluster()
    #for i in range(5):
    #    cluster.add_machine(Machine(mips=8000, speed=500, micost=8.637))
    #for i in range(5):
    #    cluster.add_machine(Machine(mips=4000, speed=500, micost=4.348))
    for i in range(10):
        cluster.add_machine(Machine(mips=3000, speed=500, micost=3.594))  # 构建虚拟机
    for i in range(10):
        cluster.add_machine(Machine(mips=2000, speed=500, micost=2.416))
    for i in range(10):
        cluster.add_machine(Machine(mips=1500, speed=500, micost=1.826))
    #for i in range(10):
    #    cluster.add_machine(Machine(mips=1000, speed=500, micost=1.237))
    #for i in range(10):
    #    cluster.add_machine(Machine(mips=500, speed=500, micost=0.648))
    #for i in range(15):
    #    cluster.add_machine(Machine(mips=250, speed=500, micost=0.353))
    
    return cluster
'''



