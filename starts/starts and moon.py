import matplotlib.pyplot as plt
import numpy as np
from random import choice
import random
import matplotlib.patches as mpatches
class randomwalk():
    def __init__(self,num_points=50):
        self.num_points=num_points
        self.x_value=[0]
        self.y_value=[0]
    def fill_walk(self):
        while len(self.x_value)<self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([0,0.05,0.1,0.15,0.2])
            x_step=x_distance*x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 0.05, 0.1, 0.15, 0.2])
            y_step = y_distance * y_direction
            if x_step==0 and y_step==0:
                continue
            next_x=self.x_value[-1]+x_step
            next_y=self.y_value[-1]+y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)

rw=randomwalk()

rw.fill_walk()
x=y=np.arange(-0.2,0.2,0.001)
x, y = np.meshgrid(x,y)

with plt.style.context(('dark_background')):
    v = ["red", "orange", "yellow", "green", "blue"]
    # 对点进行排列，可以模拟生成星带
    rw.x_value.sort()
    rw.y_value.sort()
    C1=(rw.x_value[0]+rw.x_value[-1])/2
    C2=(rw.y_value[0]+rw.y_value[-1])/2
    # 显示所有的点的散射
    for t in range(1,50):
        v1 = v[random.randint(0, 4)]
        plt.scatter(rw.x_value[t], rw.y_value[t], c=v1,marker='*', edgecolors='none', s=50)
    #模拟生成一个圆的轨迹图
    # c = mpatches.Circle((C1,C2), 0.1, facecolor="white",
    #                     edgecolor="white", alpha =1.0)
    # plt.gca().add_patch(c)

    plt.show()