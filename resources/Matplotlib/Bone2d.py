#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import  numpy as np

def shift(m ,n ,sft=0.4):
    """
    a function return shift array
    :param m: int
    calumn of destion array
    :param n: int
    row of destion array
    :param sft: float
    shift
    :return: np.ndarray
    """
    return np.random.rand(m,n) * 2 * sft - sft

def bone2d(ax, length=8, width=1, redius=2,circle_x0=6 ,number1=50, number2=200 ,sft=0.2 ,param_dict={}):
    """
    a function to draw Bone2d.py graph
    :param ax: axes
        the axes draw to
    :param length
        the length of rectangle
    :param width
        the width of rectangle
    :param redius
        the r of circle
    :param circle_x0
        the x0
    :param number1: int
         the number of dots drawed in rectangle
    :param number2: int
        the number of dots drawed in circle
    :param sft: float
        the shift of data
    :param param_dict: dict
        Dictionary of kwargs to pass to ax.plot
    :return: list
        list of artists added
    """
    # draw rectangle
    rect_x = np.random.rand(1,number1) * length - length/2 + shift(1,number1,sft)
    rect_y = np.random.rand(1,number1) * width - width/2 + shift(1,number1,sft)
    sample1 = ax.scatter(rect_x,rect_y,c='g',marker='.',label=u'样例1')
    # 显示长方形的边界
    if(param_dict.__contains__('border') and param_dict['border']==True):
        x0 = length/2;
        y0 = width/2;
        ax.plot([-x0,x0,x0,-x0,-x0],[y0,y0,-y0,-y0,y0],'g--',label=u'样例1边界')
    #draw circle1
    circle1_r = np.sqrt(np.random.rand(1,number2)) * redius
    circle1_thyta = np.random.rand(1,number2) * 2 * np.pi
    circle1_x = circle1_r * np.cos(circle1_thyta) + circle_x0 + shift(1,number2,sft)
    circle1_y = circle1_r * np.sin(circle1_thyta) + shift(1,number2,sft)
    sample2 = ax.scatter(circle1_x,circle1_y,c='r',marker='o',label=u'样例2')

    #draw circle2
    circle2_r = np.sqrt(np.random.rand(1,number2)) * redius
    circle2_thyta = np.random.rand(1,number2) * 2 * np.pi
    circle2_x = circle2_r * np.cos(circle2_thyta) - circle_x0 + shift(1,number2,sft)
    circle2_y = circle2_r * np.sin(circle2_thyta) + shift(1,number2,sft)
    sample3 = ax.scatter(circle2_x,circle2_y,c='b',marker='s',label=u'样例3')
    return [sample1,sample2,sample3]

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    ax = plt.subplot(111)
    ax.set_aspect(1)
    bone2d(ax,8,1,2,6,50,50,0.2,{'border':True})
    plt.title(u'Bone2d.py(随机扰动0.2)')
    plt.legend()
    plt.show()