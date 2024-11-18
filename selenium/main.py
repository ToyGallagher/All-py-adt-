from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import os
import time
from bs4 import BeautifulSoup
import requests
driver = webdriver.Chrome()
driver.get("https://th.trovit.com/baan/")

keyword="เชียงใหม่"
input_box = driver.find_element_by_id("what_d")
input_box.send_keys(keyword)

submit = driver.find_element_by_xpath('//*[@id="search"]/button')
submit.click()

url = driver.current_url
soup = requests.get(url)
content = BeautifulSoup(soup.content,"html.parser")


price = content.find_all("span",{"class":"actual-price"})
print(price)