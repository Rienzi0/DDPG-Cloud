from cmath import cos
import enum
from cv2 import mean
from isort import file
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def compare_1():

        methods = ["rr", "random", "earlist", "dqn","ddpg(new)"]

        resT = [[316.89, 320.73, 317.36, 294.62, 301.82, 325.4, 288.17, 305.77, 327.95, 296.94, 296.83, 279.83, 286.73, 286.79, 309.63, 312.31, 293.87, 289.97, 272.3, 274.02, 294.27, 297.82, 306.21, 303.04],
                [290.86, 291.8, 288.98, 269.03, 275.28, 298.58, 260.83, 278.03, 298.11, 272.23, 272.91, 255.88, 263.24, 263.94, 284.0, 287.94, 270.01, 269.02, 250.35, 252.67, 269.54, 274.53, 281.26, 277.39],
                [310.79, 309.72, 307.96, 287.56, 297.36, 313.91, 297.1, 299.7, 316.64, 293.89, 281.24, 270.11, 273.68, 274.54, 297.06, 301.8, 283.03, 279.01, 258.92, 260.97, 281.33, 282.21, 290.55, 291.2],
                [303.42, 322.15, 318.09, 296.37, 301.64, 322.11, 301.0, 306.92, 328.21, 303.11, 295.48, 280.33, 287.06, 289.27, 310.56, 317.68, 296.04, 293.41, 271.9, 274.0, 294.4, 297.77, 305.74, 305.12],
                [324.36, 326.28, 323.96, 301.12, 308.79, 331.76, 309.38, 314.11, 333.38, 309.13, 298.43, 284.23, 289.96, 291.11, 313.3, 317.25, 297.26, 295.37, 274.02, 276.33, 296.79, 299.09, 306.16, 306.35]]
        x = [i for i in range(len(resT[0]))]
        color = ['r','b','y','g']
        cost = [77.12902092600231,77.11713850430505,76.37507533686707,76.51076471722237,75.35322510810195]
        cpu_std = [0.12471137678656267,0.11905339138386609,0.0979047879319495,0.08950837949600027,0.04947059732810996]
        task_nums = [[178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178961, 178960, 178960, 178960, 178960, 178960],
                        [177960, 178978, 179170, 178544, 179439, 178607, 178745, 179446, 180239, 178885, 178403, 178892, 178971, 179412, 179395, 179326, 178911, 178447, 178761, 178684],
                        [194958, 195049, 194360, 194693, 194979, 192733, 193421, 192752, 193241, 193292, 175874, 176619, 175995, 175863, 176413, 151554, 151626, 151790, 151915, 152088],
                        [218990, 216937, 218585, 216547, 216324, 211478, 208901, 207048, 208734, 209822, 170280, 167632, 167913, 166542, 165685, 121900, 123047, 121310, 120540, 121000],
                        [229804, 234965, 240778, 249692, 257230, 232641, 244551, 252830, 243946, 228338, 146164, 137784, 132534, 128286, 125983, 100857, 99574, 98239, 97566, 97453]]
        #'''
        #y = [ str(i) for  i in range(1,len(task_nums[0])+1)]
        y = [i for i in range(len(resT[0]))]
        #print(y)
        #for i,name in enumerate(resT):
                #plt.plot(y,name, 'ro-', color=color[i], alpha=0.8, linewidth=1, label=methods[i])
        #'''
        plt.barh(methods,cost,color = color)
        #plt.bar(methods,cpu_std)
        plt.xlim(70,78)
        #plt.xlim(-1,21)
        #plt.ylabel("average response time ratio ")
        plt.xlabel("total cost")
        #plt.legend(loc="upper right")
        #plt.ylabel("average cpu utilization std")
        #plt.ylabel("total task nums")
        #plt.xlabel("time (every 1hr)")
        #plt.xlabel("machine number")
        plt.title("real dataset")
        plt.savefig("/Users/rienzi/Desktop/drl/实验数据/newmethods_5-200/real/pics/cost",dpi = 1000,format = "jpg")
        plt.show()
def compare_resT(resT,methods,color,filepath):
     '''
     x = [i for  i in range(len(resT[0]))]
     for i,name in enumerate(resT):
             plt.plot(x,name, 'ro-', color=color[i], alpha=1, linewidth=0.5, markersize ="3",label=methods[i])
     plt.legend(loc="upper right")
     plt.ylabel("average response time ratio")
     plt.xlabel("time (every 1hr)")
     plt.savefig(filepath + "/compare_resT",dpi = 1000,format = "jpg")
     '''
     res_list = [np.mean(i) for i in resT]
     plt.barh(methods,res_list,color = color)
     plt.xlim(300,307)
     plt.savefig(filepath + "/compare_resT_b",dpi = 1000,format = "jpg")
     #'''
     plt.show()
def compare_cost(cost,methods,color,filepath):
        '''
        x = [i for  i in range(len(cost[0]))]
        for i,name in enumerate(cost):
                plt.plot(x,name, 'ro-', color=color[i], alpha=1, linewidth=0.5, markersize ="3",label=methods[i])
        plt.legend(loc="upper right")
        plt.ylabel("average cost")
        '''
        plt.barh(methods,cost,color = color)
        plt.xlim(70,80)
        plt.savefig(filepath+"/compare_cost_b",dpi = 1000,format = "jpg")
        plt.show()


if __name__ == "__main__":

     methods=["old","only pcc","normalized double r ", "new"]
     methods2=["old","only pcc","normalized double r ","random","earliest","rr","new"]
     color = ['g',"m",'c',"b",'r','y','deepskyblue']
     resT = [[320.66, 322.93, 320.58, 299.63, 307.38, 326.9, 304.09, 308.76, 329.44, 303.79, 297.81, 282.65, 287.48, 286.7, 313.41, 315.73, 295.69, 292.26, 270.82, 272.82, 293.08, 296.21, 304.46, 303.4],
     [322.63, 324.14, 320.19, 300.04, 308.3, 327.53, 305.31, 310.26, 331.12, 304.16, 294.26, 281.75, 285.9, 286.44, 309.58, 316.23, 295.6, 292.01, 271.21, 273.91, 294.29, 296.83, 305.07, 304.6],
     [322.36, 324.42, 323.17, 300.12, 310.05, 329.09, 305.64, 311.43, 330.48, 305.24, 297.37, 281.77, 287.15, 287.9, 312.02, 316.36, 297.38, 294.46, 273.45, 274.4, 295.85, 298.97, 305.99, 305.91],
     [324.36, 326.28, 323.96, 301.12, 308.79, 331.76, 309.38, 314.11, 333.38, 309.13, 298.43, 284.23, 289.96, 291.11, 313.3, 317.25, 297.26, 295.37, 274.02, 276.33, 296.79, 299.09, 306.16, 306.35]]
     file_path = "/Users/rienzi/Desktop/drl/实验数据/newmethods_5-200/real/pics/compare"
     #compare_resT(resT,methods,color,file_path)
     cost = [75.58790642560355,75.57728074071753,75.55099959396783,77.11713850430505,76.37507533686707,77.12902092600231,75.35322510810195]
     compare_cost(cost,methods2,color,file_path)
     #compare_1()




