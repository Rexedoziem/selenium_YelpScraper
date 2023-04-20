from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm
import pandas as pd
import os
from selenium.webdriver.firefox.options import Options
import re

 # List of cities to scrape
cities = ['newyork', 'mississippi', 'illinois', 'michigan', 'houston']

for city in cities:
    url = f'https://www.yelp.com/search?cflt=bars&find_loc={city}'
    driver = webdriver.Firefox()
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(1)

    num_page = 24

    linksOflinks = []
    for i in range(0, num_page):
        time.sleep(2)
        try:
            webB = driver.find_elements(By.XPATH, ('//span[@class=" css-1egxyvc"]' or '//a[@class="css-1m051bw"]'))
        except:
            pass
        for el in webB:
            pp2 = el.find_elements(By.TAG_NAME, 'a')
            for j in pp2:
                pp3 = j.get_property('href')

            linksOflinks.append(pp3)

        try:
            driver.find_element(By.CSS_SELECTOR, '.next-link').click()
            time.sleep(3)

        except:
            break

    all_details = []
    for i in tqdm(linksOflinks):
        driver.get(i)
        img = driver.find_elements(By.XPATH, '//div[@class=" photo-header-media__09f24__ojlZt photo-header-media--overlay__09f24__KwCp5 display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"]/a/img')
        for elt in img:
            img1 = elt.get_attribute('src')

        try:
            Restaurant_name = driver.find_element(By.XPATH, '//h1[@class="css-dyjx0f"]').text
        except:
            pass
        try:
            Address = driver.find_element(By.XPATH, '//p[@class=" css-qyp8bo"]').text
        except:
            pass

        try:
            Contact_address = driver.find_elements(By.CSS_SELECTOR, 'p.css-1p9ibgf')[-3:-1]
            for l in Contact_address:
                Contact_address1 = re.sub(r'http\S+', '', l.text).strip('Ask a question')
                
        except:
            pass

        try:
            Reviews = driver.find_element(By.CLASS_NAME, 'css-1fdy0l5').text
        except:
            pass
        
        try:
            Food_name1 = driver.find_elements(By.XPATH, '//span[@class=" display--inline__09f24__c6N_k margin-r1__09f24__rN_ga border-color--default__09f24__NPAKY"]')[1:3]
            for el in Food_name1:
                Food_name = el.text.strip('$$')
        except:
            pass

        try:
            Timing = driver.find_element(By.CLASS_NAME, 'hours-table__09f24__KR8wh').text
            Timing1 = Timing.replace('\n', ' ')
        except:
            pass
        try:
            Ratings = driver.find_element(By.CLASS_NAME, 'i-stars__09f24__M1AR7').get_attribute('aria-label')
        except:
            pass
        try:
            Restaurant_url = driver.find_element(By.CSS_SELECTOR, 'div.css-1vhakgw:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(2) > a').text
        except:
            pass
        try:
            Restaurant_ownership = driver.find_element(By.XPATH, '//div[@class=" border-color--default__09f24__NPAKY nowrap__09f24__lBkC2"]/span').text
        except:
            pass


    temp={
        'image': img1,
        'Restaurant name': Restaurant_name,
        'Address': Address,
        'Contact address': Contact_address1,
        'Reviews': Reviews,
        'Dish name1': Food_name,
        'Timing': Timing1,
        'Ratings': Ratings,
        'Restaurant_url': Restaurant_url,
        'Restaurant_ownership': Restaurant_ownership,
        'url links': i
        }

    all_details.append(temp)


    data = pd.DataFrame(all_details)
    data1 = data.drop_duplicates(
    subset = [
        'image',
        'Restaurant name',
        'Address',
        'Contact address',
        'Reviews',
        'Dish name1',
        'Timing',
        'Ratings',
        'Restaurant_url',
        'Restaurant_ownership',
        'url links'], keep = False)
    save_path = os.path.join(os.getcwd(), 'yelp_folder.csv')
    data1.to_csv(save_path)

