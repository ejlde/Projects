# more like sql table or data sheet

import pandas as pd
import matplotlib.pyplot as plt

##
# creating a dataframe

data = {
    'SSN' : [123,445,511,872],
    'Name':  ['Anna','Bob','John','Mike'],
    'Age': [29,43,82,23],
    'Height': [176,165,187,182], # metric sys
    'Gender': ['f','m','m','m']
}

df = pd.DataFrame(data) # converting from dictionary to datafram
df.set_index('SSN',inplace = True) # changes from 1,2,3 ..  to SSN

#print(df) 

##
# Basic Attributes & Functions

#print(df.ndim) df.shape 
# df.size =  num of elements
# print(df.dtypes) type of each element
# print(df.T) # transpose - swap cols and rows

# print(df['Name'].iloc[1])

##
# Plotting Data 

# df['Age'].plot()
# df.hist()
# df.plot.bar()

df.Age.hist()
plt.show()