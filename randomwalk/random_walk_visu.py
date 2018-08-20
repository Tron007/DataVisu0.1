from random_walk import RandomWalk as rm 
import matplotlib.pyplot as plt

rw = rm(100)

rw.fill_walk()
#list(range(rw.num_points))
#rw.x_values
plt.figure(dpi=331,figsize=(13,6))
plt.scatter(rw.x_values,rw.y_values,linewidth=30,c=list(range(rw.num_points)),edgecolor='none',s=30,cmap=plt.cm.Blues)
plt.scatter(0,0, c = 'green', edgecolor='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)
plt.scatter(rw.x_values[len(rw.x_values)//2],rw.y_values[len(rw.y_values)//2],c='blue',edgecolor='none',s=100)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()