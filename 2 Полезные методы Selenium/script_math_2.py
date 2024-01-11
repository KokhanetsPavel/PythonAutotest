from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

txt = browser.find_element(By.ID, 'input_value')
x = txt.text
print(x)
time.sleep(5)
browser.quit()
