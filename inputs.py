from selenium import webdriver
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://the-internet.herokuapp.com/inputs")

input_text = "123321123"

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/input').send_keys(input_text)

print("Aktion ist erledig")
os.system("pause")
driver.quit()
