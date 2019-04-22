import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(50,50))

dataset=pd.read_csv('Country.csv')
#1.
# print(dataset.head(100))  #Top 100 rows
# print(dataset.describe()) #Description of Data

# sel_Data=dataset.loc[:,['Country','Landarea']]

# for i in sel_Data.itertuples():
#     if i[2]>1000:
#         print(i)

#2.
sel_Data=dataset.loc[:,['Country','GDP']]
sort_data=sel_Data.sort_index(by='GDP',ascending=False)
Sel_Sorted_Data=sort_data.iloc[:10]
plt.pie(Sel_Sorted_Data['GDP'],labels=Sel_Sorted_Data['Country'])
plt.show()