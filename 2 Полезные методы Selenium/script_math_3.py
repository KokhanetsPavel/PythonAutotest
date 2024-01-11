from selenium import webdriver
from selenium.webdriver.common.by import By
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
time.sleep(5)
browser.quit()
