from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:/Users/40020730/Downloads/ChromeDriver/chromedriver.exe")



driver.get("https://www.amazon.in/")
links_list = driver.find_elements(By.TAG_NAME, 'a')
print(len(links_list))
for ele in links_list:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))

img_list = driver.find_elements(By.TAG_NAME,'img')
for ele in img_list:
    print(ele.get_attribute('src'))