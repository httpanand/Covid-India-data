import requests
import bs4
import pandas as pd
import os

url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text,'lxml')
cases = soup.find_all('div' ,class_= 'maincounter-number')
 

data = []
for i in cases:
    span = i.find('span')
    data.append(span.string)
 
os.startfile('data.csv')
 
df = pd.DataFrame({"CoronaData": data})
df.index = ['TotalCases', ' Deaths', 'Recovered']
df.to_csv('data.csv')