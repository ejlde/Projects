import pandas as pd
import matplotlib.pyplot as plt

# Pandas Series
series = pd.Series([10,20,30,40],['A','B','C','D'])
# [values] , [indicies]
s1 = pd.Series([1,2,3,4],['a','b','c','d'])
s2 = pd.Series([7,5,1,2],['a','b','c','d'])

def mysquare(x):
    return x**2

# print(s1.apply(mysquare))

#print(s2.sort_index())
#print(s2.sort_values())
#s2.sort_values(inplace=True) # apply to actual series


#print(s1+s2) adds like indicies

#print(s1.head(2)) # first 2 rows
#print(s1.tail(2)) # last 2 rows


#print(series['C']) # returns 30

#print(series.iloc[2])

#series.name = "MySeries"
#print(dict(series)) # conversion to dictionary
# {'A':10 ...}

##
# Data visualization
s1.plot.pie()
plt.show()

# s1.to_sql() # insert to database!!!!!!!
# s1.to_string()
# s1.to_excel()
# s1.to_csv('myseries.csv')
# s1.to_json








