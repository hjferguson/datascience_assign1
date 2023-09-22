import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#convert file to dataframe
df = pd.read_csv('biostats.csv')

age_column = df['Age'].to_numpy() #df object has built in method to covert to numpy array!

#Task 3
# for age in age_column:
#     print(age)

print("Average: " + str(age_column.mean()))
print("Standard Deviation: " + str(age_column.std()))
print("Min value: " + str(age_column.min()))
print("Max value: " + str(age_column.max()))
