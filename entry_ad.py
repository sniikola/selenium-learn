from selenium import webdriver

import os
import time

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://the-internet.herokuapp.com/entry_ad")
time.sleep(3)

pop_up_header = driver.find_elements_by_xpath('//*[@id="modal"]//h3')
pop_up_text = driver.find_elements_by_xpath('//*[@id="modal"]//div[2]/p')
pop_up_close = driver.find_elements_by_xpath('//*[@id="modal"]//div[3]/p')

print("pop_up_header: " + pop_up_header.text)
print("pop_up_text: " + pop_up_header.text)
pop_up_close.clik()

print("\n#Prozess beendet\n")
os.system("pause")
driver.quit() 
