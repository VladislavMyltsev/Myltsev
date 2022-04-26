import numpy as np
import matplotlib.pyplot as plt

with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype=int)
fig, ax = plt.subplots(figsize= (16,10), dpi = 400)

data_array = data_array * tmp[1]
ax.plot(data_array)
ax.set_ylabel('Напряжение, В')
ax.set_xlabel('Время, с')
ax.set_title("График зарядки и разрядки конденсатора", pad=20.0)
print("Finish")
fig.savefig("Picture.svg")