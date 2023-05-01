from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option=Options()
option.add_experimental_option('detach',True)
driver=webdriver.Chrome("C:\drivers\chromedriver.exe",chrome_options=option)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")



#Using pixel
driver.execute_script("window.scrollBy(0,1000)","")

