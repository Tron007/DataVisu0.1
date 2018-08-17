from random_walk import RandomWalk as rm 
import matplotlib.pyplot as plt

rw = rm()

rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,c=rw.x_values,edgecolor='none',s=25,cmap=plt.cm.Blues)

plt.show()