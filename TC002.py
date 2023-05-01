from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option('detach',True)

driver = webdriver.Chrome(executable_path="C://drivers/chromedriver.exe",chrome_options=option)
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()

arrivals = driver.find_elements(By.XPATH,"//ul[@class='products']//img")

for i in range(1,len(arrivals)+1):
    arrival_name = driver.find_element(By.XPATH,"(//ul[@class='products']//img)["+str(i)+"]").get_property('title')
    print(arrival_name)
