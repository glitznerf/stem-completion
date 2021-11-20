import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit



filename = "stem_distribution_analysis.csv"
x,y = [],[]

data = np.genfromtxt(filename, dtype=int, delimiter=',', skip_header = 1)

def default_value():
    return 0

#rounded = defaultdict(default_value)

for entry in data:
    #x.append(round(entry[0]/10)*10)
    x.append(entry[0])
    y.append(entry[1])
    #x = round(entry[0]/10)*10
    #rounded[str(x)] = rounded[str(x)] + entry[1]

"""
x, y = [], []

for key, value in rounded.items():
    x.append(int(key))
    y.append(value)
"""

x = np.array(x)
y = np.array(y)

plt.xlim([0, 600])
plt.ylim([0, 1750])

plt.scatter(x, y,
    alpha=0.8,)

plt.title("Frequency of Stems")
plt.xlabel("Number of Occurences (to nearest 10th)")
plt.xlabel("Number of Occurences")
plt.ylabel("Number of Stems")

plt.show()