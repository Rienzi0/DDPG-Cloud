import numpy as np
from matplotlib import pyplot as plt
class compare(): #消融实验
    def __init__(self) -> None:
        self.pic_out = "/Users/rienzi/Desktop/drl/paper/pics"
        self.methods = ["DDPG-ver1","DDPG-ver2","DDPG-ver3","DDPG-ver4","DDPG"]
        #1-pccstd 2-dual reward 3-attention 4-normalization

        #alibaba 
        self.resT=[[387.41, 376.59, 389.94, 363.25, 390.06, 407.9, 372.93, 382.95, 395.91, 384.06, 330.93, 334.76, 369.93, 369.88, 395.94, 390.1, 342.5, 354.44, 311.25, 328.51, 357.36, 380.91, 392.97, 390.73],
        [389.33, 376.24, 390.13, 363.36, 388.47, 407.24, 370.52, 381.58, 396.5, 382.46, 330.2, 335.69, 371.49, 370.25, 393.5, 387.98, 343.09, 355.81, 311.98, 327.95, 356.18, 378.62, 391.07, 391.94],
        [387.46, 370.82, 382.28, 355.4, 379.89, 398.18, 366.19, 375.72, 387.64, 375.49, 325.62, 327.17, 363.68, 363.45, 389.35, 383.04, 335.1, 347.28, 306.09, 320.96, 349.02, 375.07, 386.67, 385.21],
        [387.35, 378.71, 393.3, 359.93, 386.34, 404.82, 369.23, 378.73, 391.94, 380.82, 331.68, 335.79, 371.16, 371.4, 396.47, 391.85, 342.74, 354.6, 312.46, 328.37, 357.53, 379.57, 391.24, 390.84],
        [389.9, 377.73, 389.58, 362.61, 387.98, 407.76, 370.88, 383.12, 395.21, 387.08, 332.55, 335.1, 372.14, 371.82, 397.82, 392.71, 344.21, 355.06, 311.24, 328.94, 359.23, 382.6, 393.21, 391.46]]
        self.cost = [217.30433001673129,217.4942840219645,219.05913435012937,217.39970756458644,217.23680596607363]
        
        #google
        self.resT=[[665.52, 177.54, 172.18, 162.46, 121.88, 136.65, 159.66, 184.53, 247.55, 194.28],
        [388.86, 181.21, 171.06, 162.94, 120.77, 136.14, 157.72, 182.05, 245.44, 190.2],
        [457.2, 179.55, 173.86, 163.1, 119.98, 135.07, 157.52, 183.75, 245.48, 191.19],
        [396.82, 177.47, 173.35, 162.47, 122.14, 136.83, 161.99, 186.25, 243.66, 190.14],
        [422.62, 177.11, 172.6, 166.94, 123.88, 138.06, 159.24, 188.87, 248.98, 195.18]]
        self.cost = [192.98820289674507,193.22605717168562,193.879252946455,193.18610880742494,192.85929529335982]

        self.cost = [i*0.15 for i in self.cost]
        #self.color = ['r','m','g','b']
        self.color = [(132/255,115/255,126/255),(245/255,192/255,141/255),(156/255,177/255,189/255),(211/255,137/255,124/255),(217/255,208/255,190/255) ]
    def compare_res(self):
        resT = []
        for i in self.resT:
            resT.append(np.mean(i))
        resT = [169.0568095124186,168.2144735287447,168.29365586252388,169.0129858597094,170.63168566945097]
        plt.figure(figsize=(8,4))
        plt.barh(self.methods,resT,color = self.color)
        plt.xlim(160,175)
        plt.axvline(resT[-1],color = 'k',ls = "--",label = str(resT[-1])[0:5])
        
        #plt.legend()
        plt.xlabel("ResTR",weight = "bold")
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        plt.xticks(weight='bold')
        plt.yticks(weight='bold')
        #plt.savefig(self.pic_out+"/g_abl_res.eps",dpi = 1000,format = "eps")
        plt.show()
    def compare_cost(self):
        plt.figure(figsize=(8,4))
        plt.barh(self.methods,self.cost,color = self.color)
        plt.xlim(190*0.15,195*0.15)
        plt.axvline(self.cost[-1],color = 'k',ls = "--",label = str(self.cost[-1])[0:5])
        
        #plt.legend()
        plt.xlabel("Cost ($)",weight="bold")
        ax=plt.gca()
        ax.spines["bottom"].set_linewidth(2)
        ax.spines["top"].set_linewidth(2)
        ax.spines["left"].set_linewidth(2)
        ax.spines["right"].set_linewidth(2)
        plt.xticks(weight='bold')
        plt.yticks(weight='bold')
        #plt.savefig(self.pic_out+"/g_abl_cost.eps",dpi = 1000,format = "eps")
        plt.show()

if __name__ == "__main__":
    c = compare()
    c.compare_cost()