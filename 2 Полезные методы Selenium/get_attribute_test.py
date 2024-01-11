from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

value = browser.find_element(By.ID, "treasure")
valuex = value.get_attribute("valuex")
x = valuex
print(x)
input = browser.find_element(By.CSS_SELECTOR, 'input[type="text"]')
y = calc(x)
input.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()
time.sleep(2)
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
time.sleep(4)