import numpy as np 
import pandas as pd 

from pandas import Series, DataFrame

df_obj_1 = DataFrame(np.arange(24).reshape(4,6))
df_obj_2 = DataFrame(np.arange(16).reshape(4,4))

concat_obj = pd.concat([df_obj_1, df_obj_2], axis=1)
drop_obj = df_obj_1.drop([0,1], axis=1)

series_obj = Series(np.arange(6))
series_obj.name = "minh"

added_column = DataFrame.join(df_obj_1, series_obj)
added_rows = added_column.append(added_column, ignore_index = True)

sorted_data = df_obj_1.sort_values(by = [5], ascending = [False])
print(sorted_data)

# work with order.csv
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