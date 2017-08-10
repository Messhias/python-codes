import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y = [x**2 for x in x_values]

plt.scatter(x_values,y,c=y,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.title("Square Numbers",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of value',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,110000])

plt.savefig('squares.png',bbox_inches='tight')
plt.show()
