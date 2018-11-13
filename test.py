import pandas as pd 
import numpy as np 

df = pd.read_csv(r"C:\Users\Minh\Desktop\Learning\Python\Pandas\order.csv")

x0 = df.groupby(['order'], as_index=False)[['ext price']].sum()
my_stat = ['count', 'mean', 'max', 'min', 'sum']
x1 = df.groupby(['order'], as_index=False)[['ext price']].agg(my_stat)
x2 = x1.reset_index()
# applying deffernt functions to defferent variables
x3 = df.groupby(['order'], as_index=False).agg({'ext price':'max', 'account':'min'})


print(x0, end='\n\n')
print(x1, end='\n\n')
print(x2, end='\n\n')
print(x3, end='\n\n')