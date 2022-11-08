# Yasin Mohammed, Ahmad Nasali bin Abd Manaf, Muhammad Syazmi bin Suhaidi, Ba Shammakh,Mazen Mohammed Ahmed, Mohamad Faisal bin Mohd Hanafi
# yaseensinbox@gmail.com, nasali.cisco@gmail.com, syazmiadi@gmail.com,mazenbashammakh1@gmail.com, faisal.hanafi90@yahoo.com


# 1. Import and Load Model
import pandas as pd
import numpy as np


#2.Read dataset
df = pd.read_csv(
    "28.-kedudukan-harga-purata-barangan-terpilih-negeri-selangor-setiap-bulan-bagi-tahun-2017-2018-processed.xslx")

# Rows and columns in dataset
df.shape

#Column labels in dataset
df.columns.to_list()

"""
#3. Pre-Processing

## Change names from Malay to English
"""

#assign new translated column labels
df.columns = ['_id', 'DESCRIPTION OF GOODS', 'UNIT', 'JANUARY', 'FEBRUARY', 'MARCH',
              'APRIL', 'MAY', 'JUN', 'JULY', 'AUGUST',
              'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

#Values under DESCRIPTION OF GOODS column
print(df['DESCRIPTION OF GOODS'].values)

#New translated values
newvals = ['Clean-Standard Chicken', 'Super-Clean Chicken', 'Live Chicken',
'Imported Turkey Chicken', 'Live Old Chicken', 'Chicken Wings',
'Bony Local Goat Meat', 'Imported Bone Mutton (Australia-Box)',
'Boneless Imported Mutton (excluding thighs-Australia)',
'Imported Bone Goat Thigh Meat (Australia)',
'Local Beef (Part 1/Thigh Meat (excluding Tenderloin))',
'Local Beef (Part 2/Solid Meat (excluding Tenderloin))',
'Local Buffalo Meat', 'Buffalo Meat Import (India) (Topside)', 
'Pork (Belly)', 'Pork (Meat & Fat/Lean & Fats)', 
'Local White Pomfret Fish (weight between 200 grams to 400 grams each)',
'Local Inflatable Fish (around 7 to 10 fishes/size M)',
'Selayang Fish (Size M)', 'Cob/Aya/Wood (Size M)',
'Large White Shrimp/Banana Prawn (Local) (around 51 to 60 prawns per kilogram)',
'Round Cabbage Import (China)', 'Tomato', 'Red-Kulai Chili',
'Green Bengal Pepper (Capsicum)', 'Coconut', 'Grated Coconut',
'Grade A Chicken Eggs (weight 65.0gm to 69.9gm each)',
'Grade B Chicken Eggs (weight 60.0gm to 64.9gm each)',
'Grade C Chicken Eggs (weight 55.0gm to 59.9gm each)',
'Imported Onions (India)', 'Red Onion Import (India-Regular)',
'Red Onion Rose Import (India)', 'Garlic Import (China)',
'Dhal Beans (Australia)', 'Imported Potatoes (China)']

#Assign new values
df['DESCRIPTION OF GOODS'] = newvals

## Dropping missing values

#Show total missing values per column
df.isnull().sum()

#Show rows with missing values
df[(df.T == 0).any()]

#Drop all the rows with missing values by reassignment
df = df[(df.T != 0).any()]

#Drop _id column
df.drop('_id', axis = 1, inplace = True)

# 4. Objective 1: To identify the essential food item that had the most consistent price in 2017

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib

from google.colab import files
df = files.upload()

import io

df = pd.read_csv(io.StringIO(df['dataset-preprocessed.csv'].decode('utf-8')))
df.head()

df_tr = df.transpose()
df_new=df_tr[2:]# remove unit and the desciption of goods
df_new.columns = df_tr.iloc[0]
df_new.head()

each_std=df_new.std() #using the std function
each_std

## What is the standard deviation for all controlled items in 2017?

sorted_each_std=each_std.sort_values()# sort the std series into low to high
sorted_each_std

## Visulaizing the standard deviation for all items.

X = [1,2,3,4] #fancy code for color
Ys = np.array([[4,8,12,16],
      [1,4,9,16],
      [17, 10, 13, 18],
      [9, 10, 18, 11],
      [4, 15, 17, 6],
      [7, 10, 8, 7],
      [9, 0, 10, 11],
      [14, 1, 15, 5],
      [8, 15, 9, 14],
       [20, 7, 1, 5]])
nCols = len(X)  
nRows = Ys.shape[0]
colors =  matplotlib.cm.rainbow(np.linspace(0, 1, len(Ys)))#because the color is cool
cs = [colors[i//len(X)] for i in range(len(Ys)*len(X))]
fig, ax = plt.subplots(figsize=(16,6)) 
each_std.plot.bar(rot=15, title="standard deviation of each items",color=cs)
plt.xticks(rotation=80)
plt.show()

## Which items top 5 items has the most consistent price in 2017?

sorted_each_std[:5] # top 5 most consistent item

fig, ax = plt.subplots(figsize=(10,6)) 
sorted_each_std[:5].plot.bar(rot=15, title="Top 5 Items with Consistent Price",color=['Grey', 'Purple', 'Blue', 'Green', 'Orange'])
plt.xticks(rotation=80)
plt.show()

"""The lower the standard deviantion, the higher the consistency of the items since the variance of the item itself is low toward changes throuhg out the year 2017

**Normal distribution complement with the standard deviation of the items that has the most consistent**
"""

fig, ax = plt.subplots(figsize=(20,20)) 
plt.subplot(3,2,1)
sns.distplot(df_new['Coconut'])
plt.legend(['Coconut '])

plt.subplot(3,2,2)
sns.distplot(df_new['Grated Coconut'], color = 'blue' )
plt.legend(['Grated Coconut'])

plt.subplot(3,2, 3)
sns.distplot(df_new['Round Cabbage Import (China)'], color = 'lime' )
plt.legend(['Round Cabbage Import (China)'])

plt.subplot(3,2,4)
sns.distplot(df_new['Dhal Beans (Australia)'], color = 'purple' )
plt.legend(['Dhal Beans (Australia) '])

plt.subplot(3,2,5)
sns.distplot(df_new['Imported Potatoes (China)'], color = 'brown' )
plt.legend(['Imported Potatoes (China)'])
plt.show()

## What are the price range of these items through out the year?

fig, ax = plt.subplots(figsize=(16,6))
plt.plot(df_new.index, df_new['Coconut'],label='Coconut',marker='x')
plt.plot(df_new.index, df_new['Grated Coconut'],label='Grated Coconut',marker='x')
plt.plot(df_new.index, df_new['Dhal Beans (Australia)'],marker='x',label='Dhal Beans (Australia)')
plt.plot(df_new.index, df_new['Round Cabbage Import (China)'],label='Round Cabbage Import (China)',marker='x')
plt.plot(df_new.index, df_new['Imported Potatoes (China)'],label='Imported Potatoes (China)',marker='x')
plt.legend()
plt.show()

# 5 Answer Question 1: The price for each items doesn't change much then it can be concluded that these items is controlled.

# 6. Objective 2: To identify the essential food item that had the least consistent price in 2017

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib

# uploading & reading the processed dataset
path = 'dataset-preprocessed.csv'
df = pd.read_csv(path)

# displaying first 5 rows
df.head()

## Data Wrangling

# this function shortens the names of the goods (removes unnecessary details enclosed within brackets)
def shorten_good_name(name):
  short_name = ''
  for c in name:
    if c == '(':
      break;
    else:
      short_name = short_name + c
  return short_name.strip()

# apply shorten_good_name to all names of goods
df['DESCRIPTION OF GOODS'] = list(map(shorten_good_name, df['DESCRIPTION OF GOODS']))

# displaying the new goods naming
df['DESCRIPTION OF GOODS']

## Data Analysis

# calculating the standard deviation of each good & storing it in a new column
df['STD'] = df.iloc[:, 2:].std(axis=1)

# extract the STD & DESCRIPTION OF GOOD columns to a new dataframe df_std
df_std = df.iloc[:, [0, len(df.columns) - 1]].sort_values(by='STD', ascending=False).transpose()

# change column names from indecies to goods name
df_std.columns = df_std.iloc[0]

# drop the first row
df_std = df_std.drop('DESCRIPTION OF GOODS', axis=0)

# change df_std from a DataFrame to a Series for plotting purposes
df_std = df_std.squeeze()

## Data Vi zualization - Standard Deviation of Goods' Prices

# plotting std of all goods
fig, ax = plt.subplots(figsize=(16,6)) 
df_std.plot.bar(rot=15, title="Fluctuation of Each Good's Price (STD)")
plt.xticks(rotation=80)
plt.show()

## Data Vizualization - Standard Deviation of Goods with Least Consistent Prices

# extracting top 5 goods with least consistent prices
top_fluctuations = df_std[:5]

# plotting STD of top 5 goods with least consistent prices
fig, ax = plt.subplots(figsize=(7,6)) 
top_fluctuations.plot.bar(rot=15, title="Fluction of Each Good's Price (STD)", color='red')
plt.xticks(rotation=80)
plt.show()

## Data Visualization - Normal Distribution & Standard Deviation of Goods with Least Consistent Price

top_goods = list(df_std.index)[:5]
top_goods

fig, ax = plt.subplots(figsize=(20,20)) 
plt.subplot(3,2,1)
sns.distplot(df[df['DESCRIPTION OF GOODS'] == top_goods[0]].iloc[:, 2:])
plt.legend([top_goods[0]])

plt.subplot(3,2,2)
sns.distplot(df[df['DESCRIPTION OF GOODS'] == top_goods[1]].iloc[:, 2:], color='green')
plt.legend([top_goods[1]])

plt.subplot(3,2, 3)
sns.distplot(df[df['DESCRIPTION OF GOODS'] == top_goods[2]].iloc[:, 2:], color='black')
plt.legend([top_goods[2]])

plt.subplot(3,2,4)
sns.distplot(df[df['DESCRIPTION OF GOODS'] == top_goods[3]].iloc[:, 2:], color='purple')
plt.legend([top_goods[3]])

plt.subplot(3,2,5)
sns.distplot(df[df['DESCRIPTION OF GOODS'] == top_goods[4]].iloc[:, 2:], color='grey')
plt.legend([top_goods[4]])
plt.show()

## Data Vizualization - 2017's Prices of Goods with Least Consistent Prices

# plotting the prices throughout 2019 of the top 5 goods with least consistent prices
fig, ax = plt.subplots(figsize=(16,6))
plt.plot(df.columns[2:14], df[df['DESCRIPTION OF GOODS'] == 'Red Onion Rose Import'].iloc[:, 2:14].squeeze(),label='Red Onion Rose Import',marker='x')
plt.plot(df.columns[2:14], df[df['DESCRIPTION OF GOODS'] == 'Large White Shrimp/Banana Prawn'].iloc[:, 2:14].squeeze(),label='Large White Shrimp/Banana Prawn',marker='x')
plt.plot(df.columns[2:14], df[df['DESCRIPTION OF GOODS'] == 'Bony Local Goat Meat'].iloc[:, 2:14].squeeze(),label='Bony Local Goat Meat',marker='x')
plt.plot(df.columns[2:14], df[df['DESCRIPTION OF GOODS'] == 'Red-Kulai Chili'].iloc[:, 2:14].squeeze(),label='Red-Kulai Chili',marker='x')
plt.plot(df.columns[2:14], df[df['DESCRIPTION OF GOODS'] == 'Green Bengal Pepper'].iloc[:, 2:14].squeeze(),label='Green Bengal Pepper',marker='x')
plt.legend()
plt.show()

# 7. Objective 3: To identify the month which had the highest net increase in prices of essential items in 2017

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset-preprocessed.csv')

#Loop to substract the values in a column with the values from the previous column
for i in reversed(range(3,14)):
  df.iloc[:,i] = df.iloc[:,i] - df.iloc[:,i-1]

#Change values of the month January to 0
df.iloc[:,2] = 0

df

#Display the net change in price for each month
df.sum()[2:,]

#Create new dataframe with month and price increases
df_Price_Increase = pd.DataFrame(list(zip(df.sum().index[2:],df.sum()[2:].values)), columns=['Month','Net Price Increase'])

#Create a bar plot of the price increases
plt.figure(figsize=(15, 8))
sns.set_theme(style="whitegrid")
plt.bar(df_Price_Increase['Month'], df_Price_Increase['Net Price Increase'], color =colors,width = 0.4)
plt.title('Net increase in prices of essential items in 2018')
plt.xlabel('Month')
plt.ylabel('Ringgit Malaysia (RM)')

# Objective 4 - Done in R