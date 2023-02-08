from selenium import webdriver
from selenium.webdriver import ActionChains
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
actionChains = ActionChains(driver)


driver.get("http://the-internet.herokuapp.com/context_menu")


hot_spot = driver.find_elements_by_id('hot-spot')
actionChains.context_click(hot_spot).perform()

alert = chrome.switch_to_alert()
print("\n#Information von Alert:\n")
print(alert.text)

alert.accept()
print("\n#Schliessen Alert:\n")

print("\n#Action Beendet\n")
os.system("pause")
driver.quit()
