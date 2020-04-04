# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:59:51 2020

@author: SID
"""

import pandas as pd
import pandas as np
import matplotlib.pyplot as plt

# Setting up the working directory
import os
retval = os.getcwd()
print ("Current working directory %s" % retval) 
os.chdir( "C:\Users\SID\Desktop\Data Analysis" )
retval = os.getcwd()
print ("Current working directory %s" % retval) 

# Reading all data files
df_uber_april = pd.read_csv('uber-raw-data-apr14.csv')
df_uber_may = pd.read_csv('uber-raw-data-may14.csv')
df_uber_june = pd.read_csv('uber-raw-data-jun14.csv')
df_uber_july = pd.read_csv('uber-raw-data-jul14.csv')
df_uber_aug = pd.read_csv('uber-raw-data-aug14.csv')
df_uber_sept = pd.read_csv('uber-raw-data-sep14.csv')
#df_uber_janjune_2015 = pd.read_csv('uber-raw-data-janjune-15.csv')

# Other Companies Data
df_Dial7 = pd.read_csv('Dial7_B00887.csv')
df_Lyft = pd.read_csv('Lyft_B02510.csv')
df_Skyline = pd.read_csv('Skyline_B00111.csv')
df_FHV = pd.read_csv('other-FHV-data-jan-aug-2015.csv')
df_Federal = pd.read_csv('Federal_02216.csv')
#df_American = pd.read_csv('American_B01362.csv')

df_Carmel = pd.read_csv('Carmel_B00256.csv')
df_Diplo = pd.read_csv('Diplo_B01196.csv')
df_FirstClass = pd.read_csv('Firstclass_B01536.csv')
df_HighClass = pd.read_csv('Highclass_B01717.csv')
df_Prestige = pd.read_csv('Prestige_B01338.csv')

# Renaming Time Columns for symmetry
#df_uber_janjune_2015.rename(columns={'Pickup_date': 'Date/Time'}, inplace=True)
df_Dial7.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_Lyft.rename(columns={'time_of_trip': 'Date/Time'}, inplace=True)
df_Skyline.rename(columns={'Date': 'Date/Time'}, inplace=True)
#df_American.rename(columns={'DATE': 'Date/Time'}, inplace=True)
df_Federal.rename(columns={'Date': 'Date/Time'}, inplace=True)

df_Carmel.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_Diplo.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_FirstClass.rename(columns={'DATE': 'Date/Time'}, inplace=True)
df_HighClass.rename(columns={'DATE': 'Date/Time'}, inplace=True)
df_Prestige.rename(columns={'DATE': 'Date/Time'}, inplace=True)




# Standardizing Date Format
#     Saving Processing time by 40x by predefining format of date. Else it takes hours just to process dates 
df_uber_april = pd.DataFrame(pd.to_datetime(df_uber_april['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.date)
df_uber_may = pd.DataFrame(pd.to_datetime(df_uber_may['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.date)
df_uber_june = pd.DataFrame(pd.to_datetime(df_uber_june['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.date)
df_uber_july = pd.DataFrame(pd.to_datetime(df_uber_july['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.date)
df_uber_aug = pd.DataFrame(pd.to_datetime(df_uber_aug['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.date)
df_uber_sept = pd.DataFrame(pd.to_datetime(df_uber_sept['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.date)
#df_uber_janjune_2015 = pd.DataFrame(pd.to_datetime(df_uber_janjune_2015['Date/Time'],format = '%Y/%m/%d %H:%M:%S').dt.date)
df_Dial7 = pd.DataFrame(pd.to_datetime(df_Dial7['Date/Time'],format = '%Y.%m.%d').dt.date)
df_Lyft = pd.DataFrame(pd.to_datetime(df_Lyft['Date/Time'],format = '%m/%d/%Y %H:%M').dt.date)
df_Skyline = pd.DataFrame(pd.to_datetime(df_Skyline['Date/Time'],format = '%m/%d/%Y').dt.date)
df_Federal = pd.DataFrame(pd.to_datetime(df_Federal[(df_Federal.Status == 'Arrived') | (df_Federal.Status == 'Assigned')]['Date/Time'],format = '%m/%d/%Y').dt.date)
#df_American = pd.DataFrame(pd.to_datetime(df_American['Date/Time'],format = '%m/%d/%Y').dt.date)

df_Carmel = pd.DataFrame(pd.to_datetime(df_Carmel['Date/Time'],format = '%m/%d/%Y').dt.date)
df_Diplo = pd.DataFrame(pd.to_datetime(df_Diplo['Date/Time'],format = '%m/%d/%Y').dt.date)
df_FirstClass = pd.DataFrame(pd.to_datetime(df_FirstClass['Date/Time'],format = '%m/%d/%Y').dt.date)
df_HighClass = pd.DataFrame(pd.to_datetime(df_HighClass['Date/Time'],format = '%m/%d/%Y').dt.date)
df_Prestige = pd.DataFrame(pd.to_datetime(df_Prestige['Date/Time'],format = '%m/%d/%Y').dt.date)


df_uber_april['company'] = 'Uber'
df_uber_may['company'] = 'Uber'
df_uber_june['company'] = 'Uber'
df_uber_july['company'] = 'Uber'
df_uber_aug['company'] = 'Uber'
df_uber_sept['company'] = 'Uber'
#df_uber_janjune_2015['company'] = 'Uber'
df_Dial7['company'] = 'Dial7'
df_Lyft['company'] = 'Lyft'
df_Skyline['company'] = 'Skyline'
df_Federal['company'] = 'Federal'
#df_American['company'] = 'American'
df_Carmel['company'] = 'Carmel'
df_Diplo['company'] = 'Diplo'
df_FirstClass['company'] = 'FirstClass'
df_HighClass['company'] = 'HighClass'
df_Prestige['company'] = 'Prestige'


# Combining All Data
df_all = pd.DataFrame()
# Uber Data
df_all = df_all.append(df_uber_april)
df_all = df_all.append(df_uber_may)
df_all = df_all.append(df_uber_june)
df_all = df_all.append(df_uber_july)
df_all = df_all.append(df_uber_aug)
df_all = df_all.append(df_uber_sept)
#df_all = df_all.append(df_uber_janjune_2015)
# Other Services Data
df_all = df_all.append(df_Dial7)
df_all = df_all.append(df_Lyft)
df_all = df_all.append(df_Skyline)
df_all = df_all.append(df_Federal)
#df_all = df_all.append(df_American)
df_all = df_all.append(df_Carmel)
df_all = df_all.append(df_Diplo)
df_all = df_all.append(df_FirstClass)
df_all = df_all.append(df_HighClass)
df_all = df_all.append(df_Prestige)

# Sorting All Values
df_all.sort_values('Date/Time',inplace=True)

# Converting All Values to Pandas datetime
df_all['Date/Time'] = pd.to_datetime(df_all['Date/Time'])

# Adding column of month for visualizations
df_all['month'] = df_all['Date/Time'].dt.month

# Uber Business vs other businesses
start_date = '2014/01/01'
end_date = '2014/12/31'
df = df_all[(df_all['Date/Time']>=start_date) & (df_all['Date/Time']<=end_date)]
df.groupby(['month','company']).count().unstack('company')['Date/Time'].plot(kind='bar', figsize = (8,6),stacked=True)
plt.ylabel('Total Journeys')
plt.title('Uber Business vs Other Businesses (2014)')

df.groupby(['month','company']).count().unstack('company')['Date/Time'].plot(figsize = (8,6),stacked=True)
plt.ylabel('Total Journeys')
plt.title('Growth of Company Businesses (2014)');
plt.grid()

-----testing-----




df_all.head(40)
df_all['DayOfWeek'] = df_all['Date/Time'].dt.weekday_name

df_all.head()


df = df_all.copy()
df.head(5)
df = df.reset_index()
#df=df.rename(columns = {'Date/Time':'Date/Time'})
import seaborn as sns
sns.set_style('whitegrid')
ax = sns.pointplot(x="DayOfWeek", y="index", hue="company", data=df)
#handles,labels = ax.get_legend_handles_labels()
#reordering legend content
#handles = [handles[1], handles[5], handles[6], handles[4], handles[0], handles[2], handles[3]]
#labels = [labels[1], labels[5], labels[6], labels[4], labels[0], labels[2], labels[3]]
ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax.set_xlabel('Day', fontsize = 12)
ax.set_ylabel('Count of Uber Pickups', fontsize = 12)
ax.set_title('Day wise Trend of Companies', fontsize=16)
ax.tick_params(labelsize = 8)
#ax.legend(handles,labels,loc=0, title="Legend", prop={'size':8})
#ax.get_legend().get_title().set_fontsize('8')
plt.show()


========================
# Uber Business in 2015
========================
1) 
start_date = '2015/01/01'
end_date = '2015/12/31'
df = df_all[(df_all['Date/Time']>=start_date) & (df_all['Date/Time']<=end_date)]
df.groupby(['month','company']).count().unstack('company')['Date/Time'].plot(kind='bar', figsize = (8,6),stacked=True)
plt.ylabel('Total Journeys')
plt.title('Uber Rides (2015)')

2) 
https://www.kaggle.com/jodielam/uber-exploratory-analysis-and-visualizations


==============================================================================

