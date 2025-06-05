import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
sns.get_dataset_names()
df = sns.load_dataset('flights')
df = df.head(50)
print(df.shape)
df.head()
df = sns.load_dataset('flights')
df = df.head(50)
print(df.shape)
df.head()
df['year'] = df['year'].astype('str')
df['month'] = df['month'].astype('str')
df['Date'] = pd.to_datetime(df['month'] + '-' + df['year'] )
df.set_index('Date',inplace=True)
df.head()
df.plot(kind='line',y='passengers',
        figsize=(10,6),
        title='Passengers x Time', xlabel='Date', ylabel='Passengers'
        )
plt.show()
(df
 .groupby(by=['year'],as_index=False)
 .agg(AvgLevels=('passengers','mean'))
 .plot(kind='line',x='year',y='AvgLevels', figsize=(5,5))
 )
plt.show()
df['Col1'] = 300 + 20 * np.random.randn(df.shape[0]) + np.random.randint(low=-10, high=20, size=df.shape[0])
df.head()
df.plot(kind='line',y=['passengers','Col1'],
        figsize=(10,6),
        title='Passengers and Col1 x Time', xlabel='Date', ylabel=' '
        )
plt.show()
"""
