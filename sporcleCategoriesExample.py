#This ended up being extremely slow with the ads... So slow I decided to start a separate project.
#However, it should work with patience!
#Creator-Ricky Marchant
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
driver.get ("https://www.sporcle.com/")
print (driver.title)
time.sleep(2)
category = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/ul/li[3]/a")
category.click()
time.sleep(3)

try:
    geographySelect = driver.find_element_by_id("geography")
    geographySelect.click()
except:
    print("SOMETHING went Awry!")
    time.sleep(2)

selectPopAllTime = driver.find_element_by_link_text("Popular All-Time").click()
countriesOfSA = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div[3]/div/div[3]/div[1]/div[13]/div/a").click()
