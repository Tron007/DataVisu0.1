import matplotlib.pyplot as plt 
inp_val = range(5,15)
squares = [x**2 for x in inp_val]

plt.scatter(inp_val,squares,c=squares,edgecolor='none',s=25,cmap=plt.cm.Blues)

plt.title("My Graph",fontsize=25)
plt.xlabel("x Value",fontsize=25)
plt.ylabel("y Value",fontsize=25)

plt.tick_params(axis='both',which='major',labelsize=25)
plt.show()