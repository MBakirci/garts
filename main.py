import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup

#initialize scraping proccess
print('Enter Google arts & culture url:')
site = input()
response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
img_og = soup.find("meta", property="og:image")

# current date and time
now = datetime.now()
timestamp = int(datetime.timestamp(now))

#filename just garts + current unix timestamp
filename = "garts-" + str(timestamp) +".jpg"

# extract url from meta tag
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(img_og))
print(urls[0])

# save to disk
with open(filename, "wb") as file:
    rsp = requests.get(urls[0])
    file.write(rsp.content)
