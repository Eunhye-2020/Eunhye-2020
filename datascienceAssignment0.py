#!/usr/bin/env python
# coding: utf-8

# In[370]:


#NAME : CHOEUNHYE NUMBER : 220202862
import requests
from bs4 import BeautifulSoup   
import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


# In[87]:


#1-1
page =requests.get("https://simple.wikipedia.org/wiki/List_of_countries_by_continents")
page


# In[88]:


soup =BeautifulSoup(page.content, 'html.parser')
print(soup)


# In[310]:


#list of continents
remove = ['References', 'Other websites']
continents=[]
continent=soup.find_all("span",class_='mw-headline')
for item in continent:
    c=item.get_text().strip()
    if c not in remove:
        continents.append(c)
print(continents) 


# In[329]:


#list of country
countries_ol= soup.findAll('ol')
countries_li= [countries.findAll('li',{'class':None , 'id':None}) for countries in countries_ol if countries.findAll('li',{'class':None}) ]
print(countries_li)


# In[344]:


countries_final= []
countries_a=[]
for c in countries_li[:len(continents)]:
    if c:
        for country in c:
            countries_a = [country.find('a').text  for country in c if country.find('a')]
        countries_final.append(countries_a)
for i in range(6,1,-1):
    countries_final[i]=countries_final[i-1]
countries_final[1]=['']
print(countries_final)


# In[337]:


#1-2
import pandas as pd


# In[354]:


df_continents = pd.DataFrame()
df_continents['continent'] = continents
df_continents


# In[355]:


df_country = pd.DataFrame()
df_country['country'] = countries_final
df_country


# In[353]:


#Create contries-continents pandas dataframe with two columns : country, continent
df_merge = pd.concat([df_continents, df_country], axis=1)
df_merge


# In[58]:


#1-3,4
import csv


# In[356]:


page =requests.get("https://en.wikipedia.org/wiki/World_Happiness_Report#2019_report")
page 


# In[74]:


soup = BeautifulSoup(page.content, "html.parser")
out = open("WorldHappinessReport.html","w", encoding="utf-8")
out.write(str(soup))
out.close()
soup=BeautifulSoup(open("WorldHappinessReport.html", encoding='utf-8'), "html.parser")
print(soup.prettify())


# In[75]:


table=soup.find('table',{'class':'wikitable sortable'})
table


# In[76]:


links=table.find_all('a')
links


# In[359]:


country =[]
for l in links:
    country.append(l.get('title'))
print(country)    


# In[360]:


df=pd.DataFrame()
df["Country"]=country
df


# In[363]:


csvFile=open("happiness.csv","wt",newline="",encoding="utf-8")
writer =csv.writer(csvFile)
try:
    for c in tr:
        th=c.find_all("th")
        th_data=[col.text.strip("\n") for col in th]
        td=c.find_all("td")
        row=[i.text.replace("\n","") for i in td]
        writer.writerow(th_data+row)
finally:
    csvFile.close()


# In[364]:


df=pd.read_csv("happiness.csv")
df


# In[365]:


#2-1 Plot the distribution of happoness score per country
plt.figure(figsize=(15,10))
plt.hist(df["Score"], bins=20)
plt.title("hapinness score per country")
plt.xlabel("happiness score")
plt.ylabel("quantity")
plt.show()


# In[369]:


#2-2 Find 10 least happy countries
print("10 least happy countries:")
print(df.sort_values(by="Score",ascending=True)[["Country or region", "Score"]].head(15).to_string(index=False))


# In[218]:


#2-3 What is the average of happiness?
average=df.Score.mean()
print('The average of happiness: ' + str(average))


# In[219]:


#2-4 What are the countries above the median 
median = df.Score.median()
print('The median of happiness score : {}'.format(median))


# In[221]:


print('The countries above the median:\n')
print(df[df['Score'] > median][['Country or region', 'Score']].to_string(index=True))


# In[197]:


#2-5 Plot the correlation between? pairs of variables 
#First pair - Country or Region and score
compare = df.groupby(['Score'])['Social support'].transform(max) == df['Social support']
df[compare][['Score','Social support']]


# In[199]:


y = df[compare]['Score']
x = df[compare]['Social support']
plt.xlabel('Social support')
plt.ylabel('Score')
plt.scatter(x,y)


# In[195]:


#Second pair - Generosity and Social Support
compare = df.groupby(['Score'])['Healthy life expectancy'].transform(max) == df['Healthy life expectancy']
df[compare][['Score','Healthy life expectancy']]


# In[200]:


y = df[compare]['Score']
x = df[compare]['Healthy life expectancy']
plt.xlabel('Healthy life expectancy')
plt.ylabel('Score')
plt.scatter(x,y)

