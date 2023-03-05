import pandas as pd
import numpy as np 

data = {
    'SSN' : [123,445,211,872],
    'Name':  ['Anna','Bob','John','Mike'],
    'Age': [29,43,82,23],
    'Height': [176,165,187,182], # metric sys [cm]
    'Gender': ['f','m','m','m']
}

df = pd.DataFrame(data)
df.set_index('SSN',inplace=True)


##
# numpy fns
#print(df['Height'].apply(np.sin)) # np.sqrt 
#
# print(df['Height'].apply(lambda x: x*100)) 
# x = all ind elements in 'Height'

##
# iterating over dataframes
#for x in df['Age']:
 #   print(x)

#for key,value in df['Age'].items(): 
 #   print("{}: {}".format(key,value))

#for row in df.iterrows():
  #  print(row)

##
# sorting by index

#df.sort_index(inplace = True) # apply changes to df
df.sort_values(by=['Age','Name'], inplace = True)
print(df)

