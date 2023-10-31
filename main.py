from selenium import webdriver
#import validators
from selenium.webdriver.common.keys import Keys
import time
import random
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()
df['link'] = ''

links = []
driver = webdriver.Chrome('.\chromedriver.exe')
i = 0
url = 'https://www.google.com/search?q=site%3Aescalatroncs.com+\"Montserrat\"'

driver.get(url+ '&start='+str(i*10))
while i<44:
    time.sleep(random.randint(10, 11))
    # grab all linkedin profiles from first page at Google

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # soup = BeautifulSoup(r.text, 'html.parser')



    search = soup.find_all('div', class_="yuRUbf")
    for j,h in enumerate(search):
        #links.append(h.a.get('href'))
        df.loc[i*10+j, 'link'] = h.a.get('href')
    #driver.find_element_by_link_text("Siguiente").click()
    i += 1
    driver.get(url+ '&start='+str(i*10))
    print (i)


df.to_csv('links3.csv')