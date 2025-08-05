import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import  LinearRegression
areas = np.array([500,540,550,600,700,800,900,1000,1100,1200]).reshape(-1, 1)
prices = np.array([150,160,170,180,190,200,210,220,230,240])
model = LinearRegression()
model.fit(areas,prices)
# Predict and Plot
plt.scatter(areas,prices,label='Data Points',color='blue')
plt.plot(areas,prices,label ='Regression Line',color='red')
plt.xlabel('Area(sq ft)')
plt.ylabel('Price of house($1000s)')
plt.title("Linear regression on house prices")
plt.legend()
plt.grid(True)
plt.show()
