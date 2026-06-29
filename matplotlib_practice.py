import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("churn.csv")

x_axis=df["tenure"]
y_axis=df["MonthlyCharges"]



z_axis=np.array([1,2,3,4,5,6,])

plt.plot(z_axis,marker="o")
plt.show()


plt.marker(z_axis,marker="*")
plt.show()





