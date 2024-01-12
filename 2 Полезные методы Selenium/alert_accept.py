from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()
time.sleep(2)

alert = browser.switch_to.alert
alert.accept()
time.sleep(2)

txt = browser.find_element(By.ID, 'input_value')
x = txt.text
print(x)

answer = browser.find_element(By.ID, 'answer')
y = calc(x)
answer.send_keys(y)

button2 = browser.find_element(By.CLASS_NAME, 'btn')
button2.click()
time.sleep(5)
browser.quit()