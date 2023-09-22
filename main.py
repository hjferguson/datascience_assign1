import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#task 1
df = pd.read_csv('biostats.csv')

#task 2
age_column = df['Age'].to_numpy() #df object has built in method to covert to numpy array!

#task 3
for age in age_column:
    print(age)

#task 4
print("Average: " + str(age_column.mean()))
print("Standard Deviation: " + str(age_column.std()))
print("Min value: " + str(age_column.min()))
print("Max value: " + str(age_column.max()))

#task5
print(np.percentile(age_column,30))
print(np.median(age_column))
print(np.percentile(age_column, 70))

#task6
plt.hist(age_column, bins=10, color='purple', edgecolor='black')
plt.title('Age Distribution - by Harlan')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.show()