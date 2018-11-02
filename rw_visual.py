import matplotlib.pyplot as plt
from random_walk import RandomWalk

#创建一个RandomWalk实例，并将其包含的点绘制出来
while True:
    rw = RandomWalk(50000)
    rw.file_walk()
    #设置窗口尺寸
    plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
                edgecolors='none',s=1)
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
                cmap=plt.cm.Blues,edgecolors='none',s=15)

    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',
                edgecolors='none',s=100 )

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break