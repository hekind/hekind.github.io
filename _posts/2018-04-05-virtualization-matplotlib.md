---
layout: post
title:  "数据可视化之matplotlib!"
date:   2018-04-05
categories: Python
tags: Virtualization Matplotlib
---

## 0. 前言
数据可视化，就是通过图形、图表等方法将原数据中的关系展示出来。

![](/styles/images/virtualization-matplotlib/mat_logo.svg)

matplotlib，是一个python下**2D绘图库**，它可以跨平台地生成各种高质量的图标。 matplotlib可以使我们很轻松地绘制如直方图、功率图、条形图和散点图等。 pyplot是matplotlib下的一个模块，它可以提供给我们类似于MATLAB的界面，可以很轻松地画出想要的图形。

![简介](/styles/images/virtualization-matplotlib/matplotlib_brief.png)

这篇文章打算介绍一些基本的方法，可以根据pyplot模块，方便快捷的画出目标图形。 暂时只打算介绍pyplot模块的状态机环境，不打算深入介绍面向对象接口(OO接口)。 这篇文章的方法应对一些普通的散点图、折线图之类的没有问题，如果以后需要更复杂的，会再写一片增补版的。 文章中涉及到的两段代码上传。

[查看](https://github.com/hekind/PythonExample/tree/master/Matplotlib "two cases")

## 1. matplotlib架构
### 1.1 matplotlib框架

![框架](/styles/images/virtualization-matplotlib/framework.png)

matplotlib框架分为三层，这三层构成了一个栈，上层可以调用下层。

- **脚本层(pyplot)**：简化了完成数据分析与可视化的常规操作。 管理创建图形、坐标轴以及他们与后端层的连接。
- **艺术家层(artist)**：管理漂亮图形背后的大多数内部活动。
- **后端层(backend)**：matplotlib的底层，实现了大量的抽象接口类；还和用户界面工具箱整合在一起；可以将图形保存为不同格式(比如PDF、PNG、PS和SVG等)。

这三层属于matplotlib程序包的范畴，脚本层(pytplot模块)可以提供给我们一个与matplotlib打交道的接口，我们可以只通过调用pyplot模块的函数从而操作整个程序包，来绘制图形。

### 1.2 编程接口

![编程接口](/styles/images/virtualization-matplotlib/code_framework.png)

第一层状态机环境，是由pyplot提供的。

第二层是有pyplot和面向对象(oo)接口提供，由pyplot获取figure对象，通过面向对象接口来显示地管理axies对象。

第三层由面向对象(oo)接口提供，该层完全不使用pyplot模块。

Python科学计算基础教程希望大家使用pyplot接口（也就是状态及环境），因为该环境封装了画图的方法，绘图非常方便。 但是官方文档希望大家使用**第一级面向对象接口**，因为该方法综合了pyplot和oo接口，是一个很好的选择。 我觉得，如果pyplot提供的功能可以满足绘图需要，直接采用即可；否则，使用后者绘图。
## 2. matplotlib的绘图概念

![图的剖析](/styles/images/virtualization-matplotlib/anatomy_of_figure.png)

一些重要的图的概念

- figure(图)，指整个图形(包括所有的元素,比如标题、线等)。 管理着所有的坐标系，还有一些特殊的艺术家和canvas(画布)。
- axes(坐标系)，数据的绘图区域。
- axis(坐标轴),坐标系中的一条轴，包含大小限制、刻度和刻度标签。
- artist(艺术家),图中所有的对象都是artis，当图形显示时，所有的艺术家都会被绘制到画布上。

![图、坐标系、坐标轴](/styles/images/virtualization-matplotlib/figure_axes_axis.png)

- 一个figure(图)可以包含多个axes(坐标系)，但是一个axes只能属于一个figure。
- 一个axes(坐标系)可以包含多个axis(坐标轴)，包含两个即为2d坐标系，3个即为3d坐标系。

## 3. matplotlib.pyplot模块
matplotlib.pytplot包含了一系列类似于matlab的画图函数。 它的函数**作用于当前图形(figure)的当前坐标系(axes)**。

> 导入:
> import matplotlib.pyplot as plt
### 3.1 plot函数
> plot(xdata,ydata,format)

参数：

- xdata:所有点的x坐标，如果不传默认是[0:]。
- ydata:所有点的y坐标。
- format:绘制的格式，默认是'b-'。比如'b-+'：分别代表颜色、线形和标记。
	- 颜色：绘制的颜色(b指blue,蓝色)。
	- 线性：点之间的连线样式(-指实线)。
	- 标记：点的风格(+为加号）。

一个例子 

	import matplotlib.pyplot as plt
	
    plt.plot([1,2],[1,2],'r--+')
	plt.show()

![格式](/styles/images/virtualization-matplotlib/format.png)

绘制出了该图，包含两个点(1,1)和(2,2)，matplotlib函数输入一般为array。

### 3.2 多重图
在绘图的时候，我们可能需要将多个子图显示在一个大图中，这时就需要多重图。
> subplot(nrows,ncols,n)

该函数返回nrow×ncols的第n个子图的坐标系(axes)，获取了坐标系对象，就可以在该子图上绘制操作。

如果这三个参数都小于10，可以省略','。 比如subplot(211)=subplot(2,1,1)，都返回如图红色的坐标系。

![子图](/styles/images/virtualization-matplotlib/subplot.png)

### 3.3 添加文本(字符串)

text(x,y,’text’)，在指定位置(x,y)，添加文本。  
xlabel(‘text’)，X轴标签。  
ylabel(‘text’)，Y轴标签。  
title(‘text’)，图形的标题。  
数学表达式：使用TeX来编写，将表达式用'$'包括，比如:

	$\sigma_i=15$

显示为

![expression](/styles/images/virtualization-matplotlib/tex_expression.gif)

![tex](/styles/images/virtualization-matplotlib/tex.png)

> TEX，是一个由美国计算机教授高德纳（Donald Ervin Knuth）编写的功能强大的排版软件。它在学术界十分流行，特别是数学、物理学和计算机科学界。TEX被普遍认为是一个优秀的排版工具，特别是在处理复杂的数学公式时。常见的发行版为LaTex。

### 3.4 pyplot的函数

pyplot提供了matplotlib绘图模块的一个访问接口，提供了一些常用的**绘图函数**,下面是一些列表，具体可以访问官网查看用法。

#### 3.4.1 函数的总结

![函数总结](/styles/images/virtualization-matplotlib/pyplot_function.png)

![绘制图形](/styles/images/virtualization-matplotlib/pyplot_function_image.png)

[http://matplotlib.org/api/pyplot_summary.html](http://matplotlib.org/api/pyplot_summary.html "官网pyplot函数总结")

#### 3.4.2 函数参数，格式(format)的总结

![格式](/styles/images/virtualization-matplotlib/pyplot_attribute.png)

[http://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot](http://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "plot参数")

#### 3.4.3 pyplot绘制模块举例

![pyplot小例子](/styles/images/virtualization-matplotlib/pyplot_instance.png)

通常我们在绘图过程中需要关注一下几个点：

1. data，也就是我们要可视化的数据，这个是最重要的，其他的都是修饰，可以没有。
2. title，标题。
3. 坐标轴标注，x、y轴的含义。
4. 刻度线，我们可以设置x、y轴的坐标，比如让它距离近一些或者远一些。也可以不管。
5. 刻度注释，对应刻度线上的标注，我们可以使用Tex来编写数学公式，是的显示的不是pi而是![pi](/styles/images/virtualization-matplotlib/tex_pi.gif)。
6. 图例，图例需要在绘制图形的时候传入label的值，最后调用lengend()来显示之前的label。

代码如下：

	# 导入模块
	import matplotlib.pyplot as plt
	import numpy as np
	
	# 准备数据
	x = np.arange(0.0, 2.0, 0.2)
	y_sin = np.sin(x)
	y_cos = np.cos(x)
	
	# 开始绘制
	plt.plot(x,y_sin,'g+-',label="Sin(x)")
	plt.scatter(x,y_cos,c='r',marker='o',label="cos(x)")
	
	# 设置图片边界
	plt.xlim(x.min()-0.2,x.max()+0.2)
	plt.ylim(y_sin.min()-0.2,y_sin.max()+0.2)
	# 设置刻度
	plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r"$\pi$",r"$-\frac{\pi}{2}$","0",r"$\frac{\pi}{2}$",r"$\pi$"])
	plt.yticks([0,1])
	# 标题
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title(u"Hello pyplot")
	plt.legend()
	
	# 显示与保存
	plt.savefig("helloplot.png")
	plt.show()

具体显示结果：

![例子](/styles/images/virtualization-matplotlib/easy_plot.png)

## 4. 绘图实例

我们想要绘制一个两边是圆，中间是线的长方形，然后他们均匀分布着三种不同的点，组成的散点图，还有一些干扰，使得一部分点可以跳出固定范围。

### 4.1 绘制方法

1. 扰动策略：生成一个array，加到点的坐标上。
2. 绘制中间长方形散点图。
3. 绘制第一个圆散点图(左圆)。
4. 绘制第二个圆散点图(右圆)。

### 4.2 代码

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

## 5. 参考文献

1. http://matplotlib.org/api/pyplot_summary.html.
2. http://matplotlib.org/tutorials/introductory/pyplot.html.
3. Hemant Kumar Mehta,陶俊杰，陈小莉.Python科学计算基础教程:123-125.
4. Vamei.绘图: matplotlib核心剖析,http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html.
5. 逝水留痕9611,一份非常好的Matplotlib教程,http://blog.csdn.net/u011497262/article/details/52325705.