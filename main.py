import matplotlib.pyplot as plt
import numpy as np


x = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.plot(x,y)
plt.show()

plt.plot(x,y,"ro") #you can replace "ro" with g^, r--, b--, b- to get different types of graphs
plt.show()

plt.plot(x,y,"g^")
plt.show()

plt.plot(x,y,"r--")
plt.show()

plt.plot(x,y,"b--")
plt.show()

plt.plot(x,y,"b-")
plt.show()

plt.plot(x,y)
plt.axis([0, 10, 0, 200])
plt.show()

plt.plot(x,y,"r--",label = "Y = X", linewidth = 5)
plt.axis([0,10,0,50])

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Sample Graph")
plt.legend()
plt.show()

x = np.arange(1,10,0.2)
print(x)
y1 = x**2
y2 = x**3
plt.plot(x,y1,"g--",x,y2,"b--")
plt.show()


x = np.linspace(-5,5,100)#generate 100 points between -5 and 5
y = 2*x + 1
plt.plot(x,y)
plt.title("Linear Graph")
plt.legend()
plt.show()

#bar graph
x= [1,3,5,7]
y= [2,6,4,9]
plt.bar(x,y,color =  "b")
plt.show()