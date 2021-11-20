import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit



filename = "total_stems_words.csv"

#data = np.genfromtxt(filename, delimiter=',', skip_header = 1)

x,y = [],[]
i = 0
skip = 10
with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        entry = line.split(",")
        if i%skip == 0:
            try:
                x.append(int(entry[0]))
                y.append(int(entry[1]))
            except ValueError:
                pass
        i += 1

print(i)

x = np.array(x)
y = np.array(y)

#plt.xlim([3000, 5700000])
plt.ylim([0, 50000])

plt.scatter(x, y,
    alpha=0.7,)

plt.title("Growth of Unique Stems")
plt.xlabel("Wordcount")
plt.ylabel("Stemcount")

plt.show()