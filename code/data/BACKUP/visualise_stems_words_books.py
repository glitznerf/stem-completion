import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit



filename = "analysis1.csv"
x,y = [],[]

data = np.genfromtxt(filename, delimiter=',', skip_header = 1)

def default_value():
    return 0

for entry in data:
    x.append(int(entry[1]))
    y.append(int(entry[2]))

x = np.array(x)
y = np.array(y)

#plt.xlim([3000, 5700000])
plt.xlim([0, 5700000])
#plt.ylim([0, 5700000])
plt.ylim([0, 45000])

plt.scatter(x, y,
    alpha=0.8,)

plt.title("Stemcount vs Wordcount in Books")
plt.xlabel("Wordcount")
plt.ylabel("Stemcount")

plt.show()