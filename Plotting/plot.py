import matplotlib.pyplot as plt
import numpy as np
import math
from math import pi
def test1():
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

def test2():
    pass

def test3():
    t = np.arange(0, 2*pi, 0.01)
    plt.plot(np.cos(t), np.sin(t), '')
    ax = plt.gca()#获取当前轴线实例
    ax.xaxis.set_ticks_position('bottom')#x轴线，使用spine中的bottom线
    ax.xaxis.set_label_coords(1,0.55)
    
    ax.yaxis.set_ticks_position('left')#y轴线，使用spine中的left线
    ax.yaxis.set_label_coords(0.5,1)

    ax.spines['bottom'].set_position(('data',0))#将bottom线的位置设置为数据为0的位置
    ax.spines['left'].set_position(('data',0))#将left线的位置设置为数据为0的位置
    ax.spines['top'].set_color('none')#将top线的颜色设置为无
    ax.spines['right'].set_color('none')#将right线的颜色设置为无
   
    plt.ylabel('sin(x)')  #labelpad='scalar')
    plt.xlabel('cos(x)')
    plt.show()

test3()