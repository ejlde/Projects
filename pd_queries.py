# how to query data from df
# how to read from csv to df

import pandas as pd

df = pd.read_csv('people.csv',delimiter=',')
df.set_index('SSN',inplace=True)

#print(df)

# SELECT NAME FROM df WHERE AGE > 40 
print(df.loc[(df['Age'] >= 45) & (df['Height'] > 170)]['Name'])
