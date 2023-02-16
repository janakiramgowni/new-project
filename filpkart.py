from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver")
driver.get("https://www.flipkart.com/search?q=ipad&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
driver.maximize_window()
driver.find_element(By.NAME,"q").clear()

time.sleep(2)
driver.find_element(By.CLASS_NAME,"L0Z3Pu").click()
driver.find_element(By.CLASS_NAME,"_4rR01T").click()
driver.get("https://www.flipkart.com/viewcart?exploreMode=true&preference=FLIPKART")
time.sleep(10)
driver.close()