import matplotlib.pyplot as plt
import numpy as np

coefficient1 = int(input("Write first coefficient: "))
coefficient2 = int(input("Write second coefficient: "))


x = np.linspace(0,100, 5)
y = coefficient1*x+coefficient2
plt.plot(x,y,label = "Graph")
plt.title("Linear Graph")
plt.legend()
plt.show()

