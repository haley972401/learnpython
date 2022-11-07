# %%
#import pandas libary
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# ## How to read file csv in pandas

# %%
#path = ('/Users/haleynguyen/Desktop/Learn Python/sales2019.csv') -- Absolute Path - another Folder
#path = ('sales2019.csv') -- Relative Path - Same Folder
#How to read file csv with pandas
path = ('sales2019.csv')
dataframe = pd.read_csv(path)
dataframe

# %% [markdown]
# ### How to merge file in pandas

# %%
df = pd.concat(map(pd.read_csv, ['sales2019_1.csv', 'sales2019_2.csv','sales2019_3.csv']), ignore_index=True)
df.to_csv('Merge_file.csv') #Create file csv with the result

# %% [markdown]
# ### Add 'Month' is a new column

# %%
path = ('Merge_file.csv')
dataframe = pd.read_csv(path)
dataframe['Month'] = dataframe['Order Date'].str.slice(0,2,1) #Slice string
print(set(dataframe['Month'])) #Print set of values of column


# %% [markdown]
# ### Get and delete some values unwanted 'nan', 'Or'

# %%
dataframe = dataframe.dropna() 
dataframe.head()
print(set(dataframe['Month']))

# %%
#df[df['Month'] == 'Or'] #Check some info of column
dataframe = dataframe[dataframe['Month'] != 'Or']
print(set(dataframe['Month']))


# %% [markdown]
# ## Reporting

# %% [markdown]
# ### 1. Which month have most revenue?

# %%
dataframe['Quantity Ordered'] = pd.to_numeric(dataframe['Quantity Ordered']) #Convert object to numeric 
#print(dataframe['Quantity Ordered'].dtypes) => Check type of column
dataframe['Price Each'] = pd.to_numeric(dataframe['Price Each'])
dataframe['Revenue'] = dataframe['Quantity Ordered'] * dataframe['Price Each']
dataframe

# %%
dataframe.groupby(by=['Month']).sum()['Revenue'] #Get revenue group by Month

# %%
sale_revenue = dataframe.groupby(by=['Month']).sum()['Revenue']
sale_revenue
print(f'{sale_revenue.idxmax()} is month have most revenue is: {sale_revenue.max()}')


# %% [markdown]
# ### 2. Which month have most revenue?

# %%
# Split after Comma - dau phay
# new_data = dataframe['Purchase Address'].str.split(',', n = 2, expand = True)
# city = new_data[1]

# Function get city name
# def getCity(sample_Adrress):
#     return sample_Adrress.split(',')[1]

# Funtion with lambda
getNameCity = lambda address: address.split(',')[1]


# %%
dataframe['City'] = dataframe['Purchase Address'].apply(getNameCity)
dataframe.head()

# %%
revenueByCity  = dataframe.groupby(by=['City']).sum()['Revenue'] #Get revenue group by city
revenueByCity.max()

# %%
#Get uni or set of column
# cities = dataframe['City'].unique()
# cities = set(dataframe['Month'])
# Nhưng truyền cities vào như hai cách trên là sẽ gây ra lỗi là trục x không trùng khớp với kết quả như trong groupby
# Do đó cách tốt nhất là lấy kết quả từ trong dữ liệu sau khi group by luôn

# cities = []
# for city, revenue in revenueByCity.items():
#     cities.append(city)

# How to write faster, how to loop through pandas
cities = [city for city, revenue in revenueByCity.items()]
print(cities)

# %%
months = range(1,3)
plt.bar(x=cities, height=revenueByCity)
plt.xlabel = 'City'
plt.ylabel = 'Revenue'
plt.xticks(cities, rotation = 45)
plt.show()

# %% [markdown]
# ### 3. What time should we display ads to maximize the likelihood of customer's buying product?

# %%
# Convert type to date
dataframe['Order Date'] = pd.to_datetime(dataframe['Order Date'])
dataframe['Hour'] = dataframe['Order Date'].dt.hour

revenueByHours = dataframe.groupby(by=['Hour']).sum()['Revenue'] #Get revenue group by Hours

hours = [hours for hours, revenue in revenueByHours.items()]

months = range(1,3)
plt.plot(hours, revenueByHours) #Get line chart
plt.grid()
plt.xlabel = 'Hours'
plt.ylabel = 'Revenue'
plt.xticks(hours, rotation = 90)
plt.show()

# %% [markdown]
# ###   Count order not by sale

# %%
# Convert type to date
dataframe['Order Date'] = pd.to_datetime(dataframe['Order Date'])
dataframe['Hour'] = dataframe['Order Date'].dt.hour

revenueByHours = dataframe.groupby(by=['Hour']).count()['Revenue'] #Get revenue group by Hours

hours = [hours for hours, revenue in revenueByHours.items()]

months = range(1,3)
plt.plot(hours, revenueByHours) #Get line chart
plt.grid()
plt.xlabel = 'Hours'
plt.ylabel = 'Revenue'
plt.xticks(hours, rotation = 90)
plt.show()

# %% [markdown]
# ### 4. What products are most sold together?

# %%
#Find duplicate productID in one order
df_dup = dataframe[dataframe.duplicated(keep=False, subset=['Order ID'])]
df_dup.head()

# %%
# dataframe['All_Product'] = df_dup.groupby('Order ID')['Product'].apply(groupProduct).reset_index()
# Không thể sử dụng apply() bởi vì khi sử dụng nó sẽ trả về một Dataframe 
# Nhưng chúng ta đang cần trả về một series vì vậy nên đổi từ apply() sang transfrorm)()
groupProduct = lambda product: ', '.join(product)
df_dup['All_Product'] = df_dup.groupby('Order ID')['Product'].transform(groupProduct)
df_dup.head()

df_dup[['Order ID','All_Product']].drop_duplicates

# %%
# df_dup['All_Product'].value_counts().head(10)
df_dup['All_Product'].explode('All_Product').value_counts()



# %%
