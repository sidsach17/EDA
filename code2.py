# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:26:06 2020

@author: SID
"""

import pandas as pd
import pandas as np
import matplotlib.pyplot as plt
from datetime import *

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
# Other Companies Data
df_Dial7 = pd.read_csv('Dial7_B00887.csv')
df_Lyft = pd.read_csv('Lyft_B02510.csv')
df_Skyline = pd.read_csv('Skyline_B00111.csv')
df_FHV = pd.read_csv('other-FHV-data-jan-aug-2015.csv')
df_Federal = pd.read_csv('Federal_02216.csv')
df_Carmel = pd.read_csv('Carmel_B00256.csv')
df_Diplo = pd.read_csv('Diplo_B01196.csv')
df_FirstClass = pd.read_csv('Firstclass_B01536.csv')
df_HighClass = pd.read_csv('Highclass_B01717.csv')
df_Prestige = pd.read_csv('Prestige_B01338.csv')

# Renaming Time Columns for symmetry
df_Dial7.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_Lyft.rename(columns={'time_of_trip': 'Date/Time'}, inplace=True)
df_Skyline.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_Federal.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_Carmel.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_Diplo.rename(columns={'Date': 'Date/Time'}, inplace=True)
df_FirstClass.rename(columns={'DATE': 'Date/Time'}, inplace=True)
df_HighClass.rename(columns={'DATE': 'Date/Time'}, inplace=True)
df_Prestige.rename(columns={'DATE': 'Date/Time'}, inplace=True)

# Standardizing Date Format
df_uber_april = pd.DataFrame(pd.to_datetime(df_uber_april['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.hour)
df_uber_may = pd.DataFrame(pd.to_datetime(df_uber_may['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.hour)
df_uber_june = pd.DataFrame(pd.to_datetime(df_uber_june['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.hour)
df_uber_july = pd.DataFrame(pd.to_datetime(df_uber_july['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.hour)
df_uber_aug = pd.DataFrame(pd.to_datetime(df_uber_aug['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.hour)
df_uber_sept = pd.DataFrame(pd.to_datetime(df_uber_sept['Date/Time'],format = '%m/%d/%Y %H:%M:%S').dt.hour)
df_Dial7 = pd.DataFrame(pd.to_datetime(df_Dial7['Time'],format = '%H:%M').dt.hour)
df_Lyft = pd.DataFrame(pd.to_datetime(df_Lyft['Date/Time'],format = '%m/%d/%Y %H:%M').dt.hour)
df_Skyline = pd.DataFrame(pd.to_datetime(df_Skyline['Time'],format = ' %H:%M ').dt.hour)
df_Federal['Time'] = (pd.to_datetime(df_Federal['Time'].str.strip(),format='%I:%M %p').dt.strftime('%H:%M')) 
df_Federal = pd.DataFrame(pd.to_datetime(df_Federal[(df_Federal.Status == 'Arrived') | (df_Federal.Status == 'Assigned')]['Time'],format = '%H:%M').dt.hour)
df_Carmel = pd.DataFrame(pd.to_datetime(df_Carmel['Time'],format = '%H:%M').dt.hour)
df_Diplo['Time'] = (pd.to_datetime(df_Diplo['Time'].str.strip(),format='%I:%M:%S %p').dt.strftime('%H:%M')) 
df_Diplo = pd.DataFrame(pd.to_datetime(df_Diplo['Time'],format = '%H:%M').dt.hour)
df_FirstClass['TIME'] = (pd.to_datetime(df_FirstClass['TIME'].str.strip(),format='%I:%M:%S %p').dt.strftime('%H:%M')) 
df_FirstClass = pd.DataFrame(pd.to_datetime(df_FirstClass['TIME'],format = '%H:%M').dt.hour)
df_HighClass['TIME'] = (pd.to_datetime(df_HighClass['TIME'].str.strip(),format='%I:%M:%S %p').dt.strftime('%H:%M')) 
df_HighClass = pd.DataFrame(pd.to_datetime(df_HighClass['TIME'],format = '%H:%M').dt.hour)
df_Prestige['TIME'] = (pd.to_datetime(df_Prestige['TIME'].str.strip(),format='%I:%M:%S %p').dt.strftime('%H:%M')) 
df_Prestige = pd.DataFrame(pd.to_datetime(df_Prestige['TIME'],format = '%H:%M').dt.hour)

df_Dial7.rename(columns={'Time': 'Date/Time'}, inplace=True)
df_Skyline.rename(columns={'Time': 'Date/Time'}, inplace=True)
df_Federal.rename(columns={'Time': 'Date/Time'}, inplace=True)
df_Carmel.rename(columns={'Time': 'Date/Time'}, inplace=True)
df_Diplo.rename(columns={'Time': 'Date/Time'}, inplace=True)
df_FirstClass.rename(columns={'TIME': 'Date/Time'}, inplace=True)
df_HighClass.rename(columns={'TIME': 'Date/Time'}, inplace=True)
df_Prestige.rename(columns={'TIME': 'Date/Time'}, inplace=True)

df_uber_april['company'] = 'Uber'
df_uber_may['company'] = 'Uber'
df_uber_june['company'] = 'Uber'
df_uber_july['company'] = 'Uber'
df_uber_aug['company'] = 'Uber'
df_uber_sept['company'] = 'Uber'
df_Dial7['company'] = 'Dial7'
df_Lyft['company'] = 'Lyft'
df_Skyline['company'] = 'Skyline'
df_Federal['company'] = 'Federal'
df_Carmel['company'] = 'Carmel'
df_Diplo['company'] = 'Diplo'
df_FirstClass['company'] = 'FirstClass'
df_HighClass['company'] = 'HighClass'
df_Prestige['company'] = 'Prestige'

# Combining All Data
df_allothers = pd.DataFrame()
df_all = pd.DataFrame()

# Uber Data
df_all = df_all.append(df_uber_april)
df_all = df_all.append(df_uber_may)
df_all = df_all.append(df_uber_june)
df_all = df_all.append(df_uber_july)
df_all = df_all.append(df_uber_aug)
df_all = df_all.append(df_uber_sept)
# Other Services Data
df_allothers = df_allothers.append(df_Dial7)
df_allothers = df_allothers.append(df_Lyft)
df_allothers = df_allothers.append(df_Skyline)
df_allothers = df_allothers.append(df_Federal)
df_allothers = df_allothers.append(df_Carmel)
df_allothers = df_allothers.append(df_Diplo)
df_allothers = df_allothers.append(df_FirstClass)
df_allothers = df_allothers.append(df_HighClass)
df_allothers = df_allothers.append(df_Prestige)

df_allothers = df_allothers.reset_index()
df = df_allothers.groupby(['Date/Time'])['company'].value_counts().unstack('company')
df1 = df.reset_index()

#FHV Vehilces
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig = plt.figure(figsize=(15,8))
plt.plot(df1['Date/Time'],df1['Carmel'],color='green')
plt.plot(df1['Date/Time'],df1['Dial7'],color='orange')
plt.plot(df1['Date/Time'],df1['Lyft'],color='blue')
plt.plot(df1['Date/Time'],df1['Skyline'],color='black')
plt.plot(df1['Date/Time'],df1['Federal'],color='red')
plt.plot(df1['Date/Time'],df1['Diplo'],color='cyan')
plt.plot(df1['Date/Time'],df1['FirstClass'],color='pink')
plt.plot(df1['Date/Time'],df1['HighClass'],color='yellow')
plt.plot(df1['Date/Time'],df1['Prestige'],color='grey')
#plt.plot(df1['index'],df1['Uber'],color='pink')

green_patch = mpatches.Patch(color='green',label='Carmel')
orange_patch = mpatches.Patch(color='orange',label='Dial7')
blue_patch = mpatches.Patch(color='blue',label='Lyft')
black_patch = mpatches.Patch(color='black',label='Skyline')
red_patch = mpatches.Patch(color='red',label='Federal')
cyan_patch = mpatches.Patch(color='cyan',label='Diplo')
pink_patch = mpatches.Patch(color='pink',label='FirstClass')
yellow_patch = mpatches.Patch(color='yellow',label='HighClass')
grey_patch = mpatches.Patch(color='grey',label='Prestige')



plt.legend(handles=[green_patch,orange_patch,blue_patch,black_patch,red_patch,cyan_patch,pink_patch,yellow_patch,grey_patch])
plt.xlabel('Hour')
plt.ylabel('Count of Journeys')
plt.title('Journeys by Hour - FHV Vehicles')
plt.show()


-----
df_all = df_all.reset_index()
df = df_all.groupby(['Date/Time'])['company'].value_counts().unstack('company')
df1 = df.reset_index()

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig = plt.figure(figsize=(15,8))
plt.plot(df1['Date/Time'],df1['Uber'],color='black')

black_patch = mpatches.Patch(color='black',label='Uber')
#plt.legend(handles=[black_patch])
plt.xlabel('Hour')
plt.ylabel('Count of Journeys')
plt.title('Journeys by Hour - Uber')
plt.show()

========================================================








import seaborn as sns
sns.set_style('whitegrid')
fig = plt.figure(figsize=(12,5))
ax = sns.pointplot(x="Date/Time", y="company", hue="company", data=df_allothers)
#handles,labels = ax.get_legend_handles_labels()
#reordering legend content
#handles = [handles[1], handles[5], handles[6], handles[4], handles[0], handles[2], handles[3]]
#labels = [labels[1], labels[5], labels[6], labels[4], labels[0], labels[2], labels[3]]
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax.set_xlabel('Hour', fontsize = 12)
ax.set_ylabel('Count of Pickups', fontsize = 12)
ax.set_title('Hour wise Trend of Services', fontsize=16)
ax.tick_params(labelsize = 8)
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
#ax.legend(handles,labels,loc=0, title="Legend", prop={'size':8})
#ax.get_legend().get_title().set_fontsize('8')
plt.show()

=======================
# Combining All Data

df_all = pd.DataFrame()

# Uber Data
df_all = df_all.append(df_uber_april)
df_all = df_all.append(df_uber_may)
df_all = df_all.append(df_uber_june)
df_all = df_all.append(df_uber_july)
df_all = df_all.append(df_uber_aug)
df_all = df_all.append(df_uber_sept)

df_all = df_all.reset_index()
import seaborn as sns
sns.set_style('whitegrid')
fig = plt.figure(figsize=(12,5))
ax = sns.pointplot(x="Date/Time", y="index", hue="company", data=df_all)
ax.set_xlabel('Hour', fontsize = 12)
ax.set_ylabel('Count of Uber Pickups', fontsize = 12)
ax.set_title('Hour wise Trend of Uber', fontsize=16)
ax.tick_params(labelsize = 8)
plt.show()