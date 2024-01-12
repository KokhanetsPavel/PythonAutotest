from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

txt = browser.find_element(By.ID, 'input_value')
x = txt.text
print(x)

answer = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
y = calc(x)
answer.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()
option2 = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()
time.sleep(2)
button = browser.find_element(By.CLASS_NAME, "btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)