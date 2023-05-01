from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option('detach',True)

driver = webdriver.Chrome(executable_path="C://drivers/chromedriver.exe",chrome_options=option)
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()

slides = driver.find_elements(By.XPATH,"//div[@class='n2-ss-slide-background']/img")

for i in range(1,len(slides)+1):
    slide_name = driver.find_element(By.XPATH,"(//div[@class='n2-ss-slide-background']/img)["+str(i)+"]").get_attribute("alt")
    print(slide_name)



