import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#convert file to dataframe
df = pd.read_csv('biostats.csv')

age_column = df['Age'].to_numpy() #df object has built in method to covert to numpy array!

