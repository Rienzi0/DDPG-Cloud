from cProfile import label
import numpy as np
from matplotlib import pyplot as plt

#####实验第一部分
class compare_1(): #google
    def __init__(self) -> None:
        self.pic_out = "/Users/rienzi/Desktop/drl/paper/pics"
        self.methods = ["rr", "random", "earlist", "DQN","DDPG"]
        self.resT = [[563.52, 182.9, 185.67, 162.27, 112.03, 126.82, 158.15, 189.97, 249.26, 186.34],
        [177.93, 161.63, 166.44, 143.59, 102.98, 115.5, 144.84, 168.29, 227.05, 167.73],
        [424.8, 173.73, 176.93, 165.1, 121.33, 134.35, 155.42, 178.89, 242.29, 195.6],
        [388.88, 162.2, 169.88, 143.83, 107.7, 118.36, 148.96, 172.84, 231.47, 170.63],
        [422.62, 177.11, 172.6, 166.94, 123.88, 138.06, 159.24, 188.87, 248.98, 195.18]]
        self.resT = [168.46280177418262,151.77724090582748,167.40176506371623,154.9696082590626,170.63168566945097]
        self.cost = [197.25997864934496,197.31371065132822,195.08925629750874,197.2963447621269,192.85929529335982]
        self.cost = [i*0.15 for i in self.cost]
        self.color = ['r','m','y','g','b']
        self.color2 = [(217/255,208/255,190/255),(132/255,115/255,126/255),(245/255,192/255,141/255),(156/255,177/255,189/255),(211/255,137/255,124/255) ]
        #self.cpu_a = [0.052050000000000006,0.0528,0.053500000000000006,0.05055,0.040400000000000005]
        self.cpu_std = [0.008327514635231811,0.008193137372215848,0.006094874896173013,0.008634813257969162,0.0025743931323712003]
        self.tasknums = [[13902, 13902, 13902, 13902, 13902, 13902, 13902, 13902, 13902, 13902, 13902, 13902, 13902, 13901, 13901, 13901, 13901, 13901, 13901, 13901],
        [13865, 13988, 13762, 13806, 13977, 13857, 13910, 14000, 13830, 13749, 13952, 13829, 14170, 13924, 13851, 13923, 13942, 13956, 13768, 13974],
        [18243, 18378, 18121, 18177, 18291, 14293, 14135, 14283, 14426, 14547, 12351, 12241, 12307, 12397, 12304, 10548, 10743, 10645, 10867, 10736],
        [11261, 13902, 14294, 15013, 14910, 14344, 13744, 13263, 13259, 12875, 13270, 12472, 15587, 13752, 14720, 16285, 13681, 14258, 14769, 12374],
        [24174, 25105, 24754, 24433, 24054, 14521, 14475, 13858, 12956, 12452, 9633, 9521, 9668, 9268, 9165, 7948, 8048, 8026, 7940, 8034]]
    def draw_res(self):
        plt.figure(figsize=(11,6))
        x_label = [ i for i in range(len(self.resT))] 
        #for i,name in enumerate(self.resT):
            #plt.plot(x_label,name, '.-', color=self.color[i], alpha=1, linewidth=3, label=self.methods[i],marker="o")
            #plt.bar(x_label,name)
        plt.barh(self.methods,self.resT,color = self.color2)
        plt.axvline(170.63168566945097,color = 'k',ls = "--")
        #plt.xlabel("time (hour)",weight='bold',fontsize=20)   
        plt.xlabel("ResTR",weight='bold',fontsize=20)  
        #plt.ylabel("ResTR",weight='bold',fontsize=20)
        #plt.legend(fontsize=13)
        plt.xlim(150,180)
        plt.xticks(weight='bold',fontsize=20)
        plt.yticks(weight='bold',fontsize=20)
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.savefig(self.pic_out+"/g_res.eps",dpi = 1000,format = "eps",bbox_inches = "tight")
        plt.show()
    
    def draw_cost(self):
        plt.figure(figsize=(11,6))
        plt.barh(self.methods,self.cost,color = self.color2)
        plt.xlim(190*0.15,200*0.15)
        plt.axvline(192.85929529335982*0.15,color = 'k',ls = "--",label = "75.35")
        #plt.legend()
        plt.xlabel("Cost ($)",weight ="bold",fontsize=20)
        plt.xticks(weight='bold',fontsize=20)
        plt.yticks(weight='bold',fontsize=20)
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.savefig(self.pic_out+"/g_cost.eps",dpi = 1000,format = "eps")
        plt.show()
    
    def draw_cpu(self):
        plt.figure(figsize=(11,6))
        plt.barh(self.methods,self.cpu_std,color = self.color2)
        
        plt.axvline(0.0025743931323712003,color = 'k',ls = "--",label = "0.049")
        plt.xlabel("Cpu Utilization STD",weight="bold",fontsize=20)
        plt.xticks(weight='bold',fontsize=20)
        plt.yticks(weight='bold',fontsize=20)
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.legend()
        #plt.savefig(self.pic_out+"/g_cpu.eps",dpi = 1000,format = "eps")
        plt.show()
    def draw_num(self):
        x_label = [ str(i) for i in range(len(self.tasknums[0]))]
        plt.figure(figsize=(8,6))
        for i,name in enumerate(self.tasknums):
            plt.plot(x_label,name, 's-', color=self.color2[i], alpha=1, linewidth=3, label=self.methods[i])
        plt.legend()
        plt.ylabel("total task number",weight ="bold")
        plt.xlabel("VM ID",weight="bold")  
        plt.xticks(weight='bold')
        plt.yticks(weight='bold')
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.savefig(self.pic_out+"/g_num.eps",dpi = 1000,format = "eps")      
        
        plt.show()
class compare_2(): #ali
    def __init__(self) -> None:
        self.pic_out = "/Users/rienzi/Desktop/drl/paper/pics"
        self.methods = ["rr", "random", "earlist", "DQN","DDPG"]
        self.resT = [[384.94, 363.79, 381.11, 353.76, 381.72, 398.57, 358.82, 374.44, 388.34, 375.44, 316.26, 321.47, 364.92, 363.16, 388.6, 380.92, 322.65, 342.68, 300.07, 319.35, 346.92, 370.15, 387.34, 382.88],
        [370.91, 349.88, 368.37, 340.48, 367.08, 386.22, 347.28, 361.32, 373.9, 363.17, 305.69, 309.85, 351.48, 350.77, 375.4, 368.2, 311.69, 331.59, 291.17, 308.53, 334.0, 360.08, 372.53, 369.11],
        [380.27, 369.98, 378.03, 351.3, 377.25, 394.28, 361.58, 371.88, 384.2, 372.0, 326.61, 326.86, 357.84, 357.62, 382.83, 380.81, 339.28, 344.44, 305.12, 319.53, 348.92, 371.4, 379.33, 379.51],
        [379.68, 358.37, 376.93, 348.15, 375.63, 393.6, 355.28, 370.03, 381.9, 370.73, 312.84, 317.46, 358.5, 357.67, 383.24, 376.62, 320.55, 340.58, 297.92, 315.7, 342.12, 367.82, 381.29, 376.74],
        [389.9, 377.73, 389.58, 362.61, 387.98, 407.76, 370.88, 383.12, 395.21, 387.08, 332.55, 335.1, 372.14, 371.82, 397.82, 392.71, 344.21, 355.06, 311.24, 328.94, 359.23, 382.6, 393.21, 391.46]]
        self.resT = [360.71182032118804,348.2626404662404,360.4765703192671,356.0577341186333,371.24864695222124]
        self.cost = [221.81218411621344,221.82615856795854,220.25431234535512,221.827337119929,217.23680596607363]
        self.cost = [i*0.15 for i in self.cost]
        self.color = ['r','m','y','g','b']
        self.color2 = [(217/255,208/255,190/255),(132/255,115/255,126/255),(245/255,192/255,141/255),(156/255,177/255,189/255),(211/255,137/255,124/255) ]
        self.cpu_a = [0.052050000000000006,0.0528,0.053500000000000006,0.0524,0.04020000000000001]
        self.cpu_std = [0.03475985471776313,0.03310528658688821,0.032173747061851526,0.033776323068090174,0.01382244551445221]
        self.tasknums = [[379968, 379968, 379968, 379968, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967, 379967],
        [379936, 379068, 380870, 379845, 379531, 379775, 380363, 380139, 379788, 380557, 378942, 380032, 380455, 378895, 381128, 378943, 380497, 380203, 378906, 381471],
        [417500, 418426, 418166, 417508, 417180, 383750, 382818, 384405, 384071, 383461, 366172, 364861, 365686, 367714, 365367, 352941, 353235, 352537, 352505, 351041],
        [377513, 379594, 377759, 379330, 378520, 379408, 379677, 379366, 379434, 381529, 380049, 381195, 379461, 380232, 380369, 380481, 381748, 382065, 380787, 380827],
        [602123, 616700, 634764, 638668, 634382, 406587, 400486, 456385, 422907, 332252, 262317, 260036, 259259, 257862, 255928, 232307, 231135, 231200, 232366, 231680]]
    def draw_res(self):
        plt.figure(figsize=(11,6))
        x_label = [ i for i in range(len(self.resT))]
        #for i,name in enumerate(self.resT):
            #plt.plot(x_label,name, '.-', color=self.color[i], alpha=1, linewidth=3, label=self.methods[i],marker="o")
        #plt.ylim(140,250)
        plt.xlim(340,380)
        plt.axvline(371.24864695222124,color = 'k',ls = "--")
        plt.barh(self.methods,self.resT,color=self.color2)
        #plt.xlabel("time (hour)",weight='bold',fontsize=20) 
        plt.xlabel("ResTR",weight='bold',fontsize=20)   
        #plt.ylabel("average ResTR",weight='bold',fontsize=20)
        #plt.legend(fontsize=13)
        plt.xticks(weight='bold',fontsize=20)
        plt.yticks(weight='bold',fontsize=20)
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.savefig(self.pic_out+"/a_res.eps",dpi = 1000,format = "eps")
        plt.show()
    def draw_cost(self):
        plt.figure(figsize=(11,6))
        plt.barh(self.methods,self.cost,color = self.color2)
        plt.xlim(210*0.15,230*0.15)
        plt.axvline(217.23680596607363*0.15,color = 'k',ls = "--")
        #plt.legend()
        plt.xticks(weight='bold',fontsize=20)
        plt.yticks(weight='bold',fontsize=20)
        plt.xlabel("Cost ($)",weight="bold",fontsize=20)
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.savefig(self.pic_out+"/a_cost.eps",dpi = 1000,format = "eps")
        plt.show()   
    def draw_cpu(self):
        plt.figure(figsize=(11,6))
        #plt.barh(self.methods,self.cpu_std,color = self.color2)
        plt.barh(self.methods,self.cpu_std,color = self.color2)
        plt.axvline(0.01382244551445221,color = 'k',ls = "--")
        plt.xlabel("Cpu Utilization STD",weight = "bold",fontsize=20)
        plt.xticks(weight='bold',fontsize=20)
        plt.yticks(weight='bold',fontsize=20)
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.legend()
        #plt.savefig(self.pic_out+"/a_cpu.eps",dpi = 1000,format = "eps")
        plt.show()
    def draw_num(self):
        x_label = [ str(i) for i in range(len(self.tasknums[0]))]
        plt.figure(figsize=(8,6))
        for i,name in enumerate(self.tasknums):
            plt.plot(x_label,name, 's-', color=self.color2[i], alpha=1, linewidth=3, label=self.methods[i])
        plt.legend()
        plt.ylabel("total task number",weight ="bold")
        plt.xlabel("VM ID",weight="bold")  
        plt.xticks(weight='bold')
        plt.yticks(weight='bold')
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        #plt.savefig(self.pic_out+"/a_num.eps",dpi = 1000,format = "eps")      
        plt.show()

        
if __name__ == "__main__":
    compare = compare_2()
    compare.draw_num()

        