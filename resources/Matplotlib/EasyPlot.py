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