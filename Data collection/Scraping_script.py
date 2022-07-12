#imports
import requests
import pandas as pd
from bs4 import BeautifulSoup
from getpass import getpass
from selenium import webdriver
import re
from tqdm import tqdm
import time
from selenium.webdriver.common.by import By

import warnings
warnings.filterwarnings('ignore')

#Headless
from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = webdriver.FirefoxOptions()
options.headless = True

#profile
profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
profile.set_preference("javascript.enabled", False);

path = './geckodriver'
driver = webdriver.Firefox(executable_path=path, firefox_profile=profile,)
# options=options)

LOGIN_URL= 'https://www.drugs.com/account/login/'
driver.get(LOGIN_URL)

usernameInput = driver.find_element(By.NAME,"username")
passwordInput = driver.find_element(By.NAME,"password")

print('Sign in or Create an account at \nhttps://www.drugs.com/account/register/')

username = input('Enter username: ')
password = getpass('Enter password: ')

#enter username and password
usernameInput.clear()
usernameInput.send_keys(username)
passwordInput.clear()
passwordInput.send_keys(password)
button = driver.find_element(By.XPATH,'//input[contains(@value, "Sign In")]').click()

names = []
reviews = []
conditions = []
ratings = []

drugs = ['lisinopril','metoprolol','amlodipine','losartan','furosemide']
for drug in tqdm(drugs, desc='scraping www.drugs.com....'):
    url = f'https://www.drugs.com/comments/{drug}/?page=1'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    wrapper=soup.findAll('div', class_='ddc-comment ddc-box ddc-mgb-2')
    x=soup.findAll('meta')[2]['content']
    pageNumber=round(int(re.findall("\d\d\d",x)[0])/int(len(wrapper)))

    for number in range(pageNumber):
        url = f'https://www.drugs.com/comments/{drug}/?page={number}'
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        wrapper=soup.findAll('div', class_='ddc-comment ddc-box ddc-mgb-2')

        for i in wrapper:
            names.append(soup.h1.text.split()[3])
            reviews.append(i.p.text.split('\t\t')[1])
            conditions.append(i.p.text.split('\t\t')[0])
            try:
                ratings.append(i.find('div', class_="ddc-rating-summary ddc-mgb-1").text.split('/')[0])
            except AttributeError:
                ratings.append('1')
df=pd.DataFrame({
    'drug':names,
    'condition':conditions,
    'review':reviews,  
    'rating':ratings, 
})
df.to_csv('./Datasets/drugs.csv', index=False)
print('Done-----------www.drugs.com')
    
names = []
reviews = []
effects=[]
conditions = []
ratings = []

drugs = ['LISINOPRIL','METOPROLOL+SUCCINATE','METOPROLOL+TARTRATE','NORVASC','COZAAR', 'LASIX']
codes=[76180, 76640, 73288, 19787, 20386, 16273 ]
for drug, code in tqdm(zip(drugs, codes), desc='scraping www.askapatient.com....'):
    baseUrl = f'https://www.askapatient.com/viewrating.asp?drug={code}&name={drug}'
    driver.get(baseUrl)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    pageNumber = int(soup.find('div', id='searchResultsDetailHeader').findAll('a')[-1].text)

    for number in range(pageNumber):

        url = f'{baseUrl}&page={number}'
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        wrapper = soup.findAll('tr')[3:]
        if number % 4==0:
            time.sleep(10)


        for i in wrapper:
            names.append(drug)
            reviews.append(f"{i.findAll('td')[2].text.strip()}")
            conditions.append({i.findAll('td')[3].text.strip()})
            effects.append(i.findAll('td')[1].text.strip())
            ratings.append(i.findAll('td')[0].text.strip())
   
df=pd.DataFrame({
    'drug':names,
    'condition':conditions,
    'effect':effects,
    'review':reviews,  
    'rating':ratings, 
})

df.to_csv('./Datasets/askapatient.csv', index=False)
print('Done-----------www.drugs.com')



