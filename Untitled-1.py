# %%
#import pandas libary
import pandas as pd

# %%
#path = ('/Users/haleynguyen/Desktop/Learn Python/sales2019.csv') -- Absolute Path - another Folder
#path = ('sales2019.csv') -- Relative Path - Same Folder
#How to read file csv with pandas
path = ('sales2019.csv')
dataframe = pd.read_csv(path)
dataframe

# %% [markdown]
# #How to merge file csv with pandas

# %%
df = pd.concat(map(pd.read_csv, ['sales2019_1.csv', 'sales2019_2.csv','sales2019_3.csv']), ignore_index=True)
df.to_csv('Merge_file.csv') #Create file csv with the result

# %%
path = ('Merge_file.csv')
df = pd.read_csv(path)
df['Month'] = df['Order Date'].str.slice(0,2,1) 
print(set(df['Month'])) #Print set of values of column


# %% [markdown]
# ### Get and delete some values unwanted 'nan', 'Or'
# 


