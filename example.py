import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns


print("Hello Programmer")

x1=np.arange(1,6)
y1=x1*2
y2=x1**2

print(x1)
print(y1)
print(y2)

plt.plot(x1,y1,marker='*',color='red')
plt.plot(x1,y2,marker='D',color='green')

