import matplotlib.pyplot as plt
measured_data = [12, 48, 75, 57, 54, 47]
plt.plot(measured_data)
# plt.show()

measured_data_str = [str(item) for item in measured_data]

with open("data.txt", "w") as outfile:
    outfile.write("\n".join(measured_data_str))
