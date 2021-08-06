import time
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup
import pandas as pd

hikes = []  # List to store name of the trail
cities = []  # List to store city of the trail

# load the driver
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# get the web page
driver.get('https://www.alltrails.com/germany/bavaria');
time.sleep(20)

time.sleep(20)

# click the button exactly 8 times
for n in range(57):
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div[2]/div[2]/div/button').click()
    s = randint(1, 10)
    time.sleep(s)

# stick-bar-parent > div.styles-module__section___20Yip > div.styles-module__showMore___2Bhtr > div > button
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
for a in soup.findAll('div', attrs={
    'class': 'styles-module__content___1eARw styles-module__content___3dWXB styles-module__descriptive___3ATWV'}):
    title = a.find('div', attrs={'class': 'xlate-none styles-module__name___3T41O undefined'})
    city = a.find('a', attrs={
        'class': 'xlate-none styles-module__location___11FHK styles-module__info___1Mbn6 styles-module__link___3T9FO'})
    hikes.append(title.text)
    cities.append(city.text)

driver.quit()

df = pd.DataFrame({'trail': hikes, 'city': cities})
df.to_csv('hikes_v2.csv', index=False, encoding='utf-8')
