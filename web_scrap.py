#Web scraping

import requests
from bs4 import BeautifulSoup
import pandas

url = "https://www.newegg.com/global/in-en/Cell-Phones/Category/ID-450"

req = requests.get(url)
content = req.content
scraped_info_list = []

soup = BeautifulSoup(content, "html.parser")

all_mobile = soup.find_all("div", {"class":"item-cells-wrap"})

for mobile in all_mobile:
    mobile_dict = {}
    mobile_dict["name"] = mobile.find("a", {"class":"item-title"}).text
    mobile_dict["price"] = mobile.find("li", {"class":"price-current"}).text
    #print(mobile_name,mobile_price)
    
    scraped_info_list.append(mobile_dict)

dataFrame = pandas.DataFrame(scraped_info_list)

dataFrame.to_csv("mobile.csv")
