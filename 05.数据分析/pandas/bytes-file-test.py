import pandas as pd

a = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})
a.to_pickle('test')

b = pd.read_pickle('test')

print type(b)
print b 
