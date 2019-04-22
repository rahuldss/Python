import numpy
import pandas

# arr=numpy.array([5,6,7])
# series=pandas.Series(arr)
# print(series)

# data_dict={'a':1,'b':2,'c':3}
# series=pandas.Series(data_dict)
# print(series)

# listx=[10,20,30,40]             #Default column name will be printed
# table=pandas.DataFrame(listx)
# print(table)

# listx=[{'Name': 'Abc', 'Age':20},{'Name': 'Def', 'Age':25},{'Name': 'Xyz', 'Age':30}]   #Column Names provided
# table=pandas.DataFrame(listx)
# print(table)

# table=pandas.DataFrame(listx,index=['row-1','row-2','row-3'])
# print(table)

# series1=pandas.Series([40,50,60],index=['maths','physics','chem'])
# series2=pandas.Series([45,55,65],index=['maths','physics','chem'])
# table=pandas.DataFrame({
#     'Jim':series1
#     ,'Carry':series2
#     ,'Pam':pandas.Series([45,55,65,67,88],index=['maths','physics','chem','C++','English'])   #Adding new row with new Subjects
# })

# #table['Pam']=pandas.Series([45,55,65,67,88],index=['maths','physics','chem','C++','English'])   #Adding new row 
#                                                                                     #but new subject is not included
# print(table)
# del(table['Jim'])   #Delete the Jim
# print(table)

# print(table.loc['maths'])   #Return the data for Maths only

# print(table.iloc[1])        #Print the row

# table.append(pandas.DataFrame([[30,45,67]],columns=['Jim','Carry','Pam']))
# print(table)

# table_read=pandas.read_csv('arr1.csv')
# print(table_read)
# table_read.to_csv('arr2.csv')

# # ***GROUP BY OPERATION***
# world_cup={'Team':['India','Australia','Sri Lanka','India'],
#             'Rank':[7,6,5,8],
#             'Year':[1987,1989,2001,2009]
# }
# df=pandas.DataFrame(world_cup)
# print(df)
# print(df.groupby('Team').groups)
# print(df.groupby(['Team','Rank']).groups)

# print('============================================================')
# for name,group in df.groupby('Team'):
#     print('Group Name : ',name)
#     print(group)
#     print('==============================')
# print('============================================================')
# for name,group in df.groupby('Team'):
#     print('Group Name : ',name)
#     print(group['Year'])
#     print('==============================')

# ***CONCATENATION OPERATION***
world_cup={'Team':['India','Australia','Sri Lanka','India'],
            'Rank':[7,6,5,8],
            'Champian_Year':[2011,1999,1986,2005],
            'Year':[1987,1989,2001,2009]
}
chokers={'Team':['India','Australia','Sri Lanka','India'],
            'Rank':[7,6,5,8],
            'Year':[1987,1989,2001,2009]
}
df1=pandas.DataFrame(world_cup)
df2=pandas.DataFrame(chokers)
print(pandas.concat([df1,df2]))
print(pandas.merge(df1,df2,on='Team'))
print(pandas.merge(df1,df2,on='Team',how='left'))
print(pandas.merge(df1,df2,on='Team',how='right'))