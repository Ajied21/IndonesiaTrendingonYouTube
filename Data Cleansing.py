#Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""#Load"""

from google.colab import drive
drive.mount ('/content/drive')

pd.options.display.max_columns=999
file = pd.read_csv('/content/drive/My Drive/Colab Notebooks/trending.csv', low_memory=False)

"""#Read"""

file.head()
#file.tail()
#file.sample(5)

"""#More Information"""

#file.info
#file.shape
#file.size
#file.columns
file.dtypes

"""#Data Cleaning"""

file.isnull().sum()

file = file.drop(['video_id', 'channel_id', 'thumbnail_url', 'thumbnail_width', 'thumbnail_height', 'category_id', 'allowed_region', 'blocked_region', 'dimension'],axis=1)

file = file.drop(['favorite', 'license_status', 'tags', 'definition', 'caption'],axis=1)

file = file.drop(['live_status'],axis=1)

file.isna().sum()

file = file.dropna()
file.shape

file = file.sort_values('view',ascending=False).drop_duplicates(subset=['title','channel_name'],keep='first')
file.shape

"""#Data Engineering"""

file_1 = file.copy()
file_1.sample(2)

file_1.loc[:,'publish_time'] = pd.to_datetime(file_1.publish_time.str.replace('Z','').str.replace('T',' '))

file_1.head(2)

file_1[file_1['publish_time'].dt.year!=2021]

file_2 = file_1.copy()

file_2.loc[:,'publish_month'] = file_2.loc[:,'publish_time'].apply(lambda x:(pd.to_datetime(x).month))

file_2.columns.values

file_2 = file_2[['publish_time','publish_month','channel_name', 'title', 'local_title', 'local_description',
       'description', 'duration', 'view', 'like', 'dislike', 'comment', 'trending_time',
       ]]

file_2['duration'] = file_2['duration'].apply(lambda x:x.replace('PT',''))

def duration_clear(x):
    try:
        if ('H' in x) & ('M' in x) & ('S' in x):
            for r in (("H", ":"), ("M", ":"), ("S", "")):
                x = x.replace(*r)
            hours = (pd.to_datetime(x,format='%H:%M:%S').time().hour)*60
            minut = pd.to_datetime(x,format='%H:%M:%S').time().minute
            second = (pd.to_datetime(x,format='%H:%M:%S').time().second)/60
            return  float(hours+minut+second)
        elif ('H' in x) & ('M' in x) :
            for r in (("H", ":"), ("M", "")):
                x = x.replace(*r)
            hours = (pd.to_datetime(x,format='%H:%M').time().hour)*60
            minut = pd.to_datetime(x,format='%H:%M').time().minute
            return float(hours+minut)
        elif ('H' in x) & ('S' in x):
            for r in (("H", ":"), ("S", "")):
                x = x.replace(*r)
            hours = (pd.to_datetime(x,format='%H:%S').time().hour)*60
            second = (pd.to_datetime(x,format='%H:%S').time().second)/60
            return float(hours+second)
        elif ('H' in x):
            for r in (("H", ""),):
                x = x.replace(*r)
            return float((pd.to_datetime(x,format='%H').time().hour)*60)
        elif ('M' in x) & ('S' in x):
            for r in (("M", ":"),("S", "")):
                x = x.replace(*r)
            minute = pd.to_datetime(x,format='%M:%S').time().minute
            second = (pd.to_datetime(x,format='%M:%S').time().second)/60
            return float(minute+second)
        elif ('M' in x):
            for r in (("M", ""),):
                x = x.replace(*r)
            return float(pd.to_datetime(x,format='%M').time().minute)
        elif ('S' in x):
            for r in (("S", ""),):
                x = x.replace(*r)
            return float((pd.to_datetime(x,format='%S').time().second)/60)
    except:
        return float('NaN')

file_2['duration (minutes)'] = file_2['duration'].apply(lambda x: np.round(duration_clear(x),2))
file_2 = file_2.drop('duration',axis=1)

file_2.sample(2)

file_2['duration (minutes)'].isna().sum()

file_2 = file_2.dropna()
file_2.info()

file_2.isna().sum()

file_2.to_csv('Youtube trend.csv', index= False)

file_2.head()