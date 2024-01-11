from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def sum(x, y):
  return str(x + y)

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, "num1")
num2 = browser.find_element(By.ID, "num2")
x = int(num1.text) + int(num2.text)
print(x)
time.sleep(2)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(x)) # ищем элемент с суммой num1+num2
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
time.sleep(4)
browser.quit()
