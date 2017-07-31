import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares=[1,4,8,16,25]
plt.plot(input_values,squares,linewidth=5)

plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Value",fontsize=14)

plt.tick_params(axis="both", labelsize=14)

plt.show()
