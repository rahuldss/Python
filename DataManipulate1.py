import pandas as pd
import numpy as np

# df=pd.DataFrame({'a':pd.Series(np.arange(1,103)),'b':pd.Series(np.arange(1,101))})
# print(df)
# print(df.axes)

# df=pd.DataFrame({'a':pd.Series(np.arange(1,103))})
# print(df.values)

# df=pd.DataFrame({'a':pd.Series(np.arange(1,103)),'b':pd.Series(np.arange(1,101))})
# print(df.head())    #Default is 5
# print(df.head(10))
# print(df.tail(10))
# print(df.sum())
# print(df.std())

# df=pd.DataFrame({'Odd':np.arange(1,100,2),'Even':np.arange(0,100,2)})
# print(df)

df=pd.DataFrame(np.random.randn(5,4),columns=['col-1','col-2','col-3','col-4'])
for key,value in df.iteritems():
    #print(key,value)
    print('Key : ',key)
    print('Value : ',value,type(value))