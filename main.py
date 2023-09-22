#Harlan Ferguson 101133838
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

#task 5 and 6 -i figured the percentiles where more valuable in the graph than they were in the console output
percentiles = np.percentile(age_column, [30, 50, 70]) #50th percentile is median
colours = ['red', 'green', 'blue'] #for clarity, each percentile line will be a different colour
legend_labels = [f'{int(percentiles[0])} (30th percentile)', f'{int(percentiles[1])} (median)', f'{int(percentiles[2])} (70th percentile)'] #I was having trouble generating labels during the enumerate
                                                                                                                                            #so this is the most simple way of making good labels

# Add vertical lines for percentiles
for i, percentile in enumerate(percentiles):
    plt.axvline(x=percentile, color=colours[i], linestyle='--') #axvline built in method for verticle lines. I pass the xloc, what colour i want it to be, and to make it dashed. 


plt.hist(age_column, bins=10, color='purple', edgecolor='black') #from the assignment doc, it looked like bins were 10 so i copied the same
plt.title('Age Distribution - by Harlan')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend(legend_labels, loc='upper right') #since i merged task 5 and 6, legend makes the chart more readable 

plt.show()