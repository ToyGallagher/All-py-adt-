from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

import time

loginURL = 'https://accounts.google.com/v3/signin/identifier?dsh=S302039529%3A1664353064300723&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fhl%3Dth&ec=GAlAwAE&hl=th&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession'

###################################################################

#Fill in Email and Password
email = 'chanthawat.aph@student.sk.ac.th '
password = '1102003620921 '
meetURL = ' https://meet.google.com/dkf-uagq-yxe?authuser=6&pli=1'

###################################################################
options = Options()
options.add_argument('--disable-infobars')
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('use-fake-device-for-media-stream')
options.add_argument('use-fake-ui-for-media-stream')
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
})

driver = webdriver.Chrome(options=options)
driver.get(loginURL)

loginField = driver.find_element_by_id('identifierId').send_keys(email)
nextBTN = driver.find_element_by_id('identifierNext').click()

WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'passwordNext')))
time.sleep(3)

pyautogui.click(x=818, y=575)
pyautogui.write(password)

passwordBTN = driver.find_element_by_id('passwordNext').click()

WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'gb')))
time.sleep(3)

# go to meet 
print('\n'*15)
driver.get(meetURL)

micBTN = driver.find_element_by_class_name('ZB88ed')
micStatus = micBTN.find_element_by_class_name('U26fgb').get_attribute('data-is-muted')
if(micStatus == 'false'):
    print('Mic\'s on, turning off')
    micBTN.click()
    
camBTN = driver.find_element_by_class_name('GOH7Zb')
camStatus = camBTN.find_element_by_class_name('U26fgb').get_attribute('data-is-muted')
if(camStatus == 'false'):
    print('Cam\'s on, turning off')
    camBTN.click()

joinBTN = driver.find_element_by_class_name('uArJ5e')
joinBTN.click()