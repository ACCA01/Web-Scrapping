# -*- coding: utf-8 -*-
"""Program.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14l8ORBBHk-vDbSNKfTT2c-QZMel6HQj-
"""

import requests
from csv import writer

url = "https://www.worldometers.info/gdp/nepal-gdp/"

html = requests.get(url).content

print(html)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

print(soup)

GDP_Table = soup.find(class_ = 'table')
GDP_Table

rows = GDP_Table.find_all('tr')

rows[0]

Year = [item.find('td').text for item in rows[1:]]
GDP_Nominal = [item.find('td').text for item in rows[1:]]
GDP_Real = [item.find('td').text for item in rows[1:]]
GDP_Change = [item.find('td').text for item in rows[1:]]
GDP_Per_Capita = [item.find('td').text for item in rows[1:]]
POP_Change = [item.find('td').text for item in rows[1:]]
Population = [item.find('td').text for item in rows[1:]]

Year

data = {
    "Year" : Year,
    "GDP_Nominal" : GDP_Nominal,
    "GDP_Real" : GDP_Real,
    "GDP_Change" : GDP_Change,
    "GDP_Per_Capita" : GDP_Per_Capita,
    "POP_Change" : POP_Change,
    "Population" : Population
}

for row in rows[:]:
  cells = row.find_all(['td', 'th'])
  cells_text = [cell.get_text(strip = True) for cell in cells]
  print(cells_text)

import pandas as pd

df = pd.DataFrame(data)

df.head()

df.tail()

df.to_csv('data.csv', index=False)

