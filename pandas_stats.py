import pandas as pd
import matplotlib as plt

data = {
    'SSN' : [123,445,511,872],
    'Name':  ['Anna','Bob','John','Mike'],
    'Age': [29,43,82,23],
    'Height': [176,165,187,182], # metric sys [cm]
    'Gender': ['f','m','m','m']
}

df = pd.DataFrame(data)
df.set_index('SSN',inplace=True)

# print(df['Age'].count()) #.sum .prod 

# avg height
#print(df['Height'].mean()) #.median() , .mode = most often
# .std
# .min .max

print(df['Height'].describe())  # percentiles


