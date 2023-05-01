from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option=Options()
option.add_experimental_option('detach',True)
driver=webdriver.Chrome("C:\drivers\chromedriver.exe",chrome_options=option)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")



# Using ExecuteScript till particular ele
subscribe_ele=driver.find_element(By.XPATH,"//input[@value='Subscribe']")
driver.execute_script("arguments[0].scrollIntoView();",subscribe_ele)


#Till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")