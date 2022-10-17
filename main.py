import requests

from replit import db
import sqlalchemy

import pandas as pd
import numpy as np


#define variables, could add others for maxPrice etc

#https://www.reddit.com/r/webscraping/comments/wjb8uv/rightmove_scraping/


boroughs = {
    "Lambeth": "5E93971",
    #"Southwark": "5E61518",
    }

pages = 10

# define our user headers
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

output = []
for name,borough_code in boroughs.items():
    for page in range(1,pages+1):
        url = f"https://www.rightmove.co.uk/api/_search?locationIdentifier=REGION%{borough_code}&numberOfPropertiesPerPage=24&radius=0.0&sortType=2&index={str(24*page)}&maxBedrooms=3&minBedrooms=2&maxPrice=550000&minPrice=475000&sortType=6&propertyTypes=&includeSSTC=false&viewType=LIST&channel=BUY&areaSizeUnit=sqft&currencyCode=GBP&isFetching=false"
        print(f'Scraping: {name} - Page: {page}')
        data = requests.get(url,headers=headers).json()
        properties = data['properties']
        output.extend(properties)

df = pd.json_normalize(output)

df.to_csv('scraped_data.csv',index=False)

df1 = pd.DataFrame(df)
db["key"] = df1
#print(df1)

#https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=ME15&useLocationIdentifier=false&locationIdentifier=&buy=For+sale




#https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&
#locationIdentifier=OUTCODE%5E1614&
#insId=1&
#radius=0.0&
#minPrice=&
#maxPrice=&
#minBedrooms=&
#maxBedrooms=&
#displayPropertyType=&
#maxDaysSinceAdded=&
#_includeSSTC=on&
#sortByPriceDescending=&
#primaryDisplayPropertyType=&
#secondaryDisplayPropertyType=&
#oldDisplayPropertyType=&
#oldPrimaryDisplayPropertyType=&
#newHome=&
#auction=false


