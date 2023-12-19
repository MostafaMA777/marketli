from selenium import webdriver
from time import sleep
import os
import pandas as pd
import datetime

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://marketlii.com/dashboard/sensor')
driver.find_element("css selector", "#intro button.blogin").click()
driver.find_element("name", "username").send_keys("hanywawe@gmail.com")
driver.find_element("name", "password").send_keys("mciwlEEWkdjD54%3@Idh")
driver.find_element("css selector", "input[type=\"submit\"]").click()
driver.get('https://marketlii.com/dashboard/sensor')
while True:
    dates = []
    users = []
    products = []
    cities = []
    links = []
    all = driver.find_element("xpath", f'/html/body/div[2]/div[2]/div[2]').text
    list = all.splitlines()
    K = 'PLUS |🚀'
    while(K in list):
        list.remove(K)
    
    R = int(len(list) / 4) + 1
    name = datetime.datetime.now().strftime("%m-%d-%Y %H.%M.%S")
    
    for i in range(1, R):
        date = driver.find_element("xpath", f'/html/body/div[2]/div[2]/div[2]/div[{i}]/div[1]').text
        user = driver.find_element("xpath", f'/html/body/div[2]/div[2]/div[2]/div[{i}]/div[2]').text
        product = driver.find_element("xpath", f'/html/body/div[2]/div[2]/div[2]/div[{i}]/div[3]').text
        product = product.replace('PLUS |🚀', '').strip()
        link = 'https://marketlii.com/dashboard/product' +'/' + product
        city = driver.find_element("xpath", f'/html/body/div[2]/div[2]/div[2]/div[{i}]/div[4]').text
    
        dates.append(date)
        users.append(user)
        products.append(product)
        links.append(link)
        cities.append(city)

    data = {
    'Date': dates,
    'User': users,
    'Product': products,
    'Link': links,
    'City': cities
    }
    df = pd.DataFrame(data)
    df.to_csv(f'sensor/1{name}.csv', index=False, encoding="utf-8-sig")
    sleep(1800)