from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
input1.send_keys("Pavel")
input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
input2.send_keys("Kokhanets")
input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
input3.send_keys("pkok@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file_download.txt')           # добавляем к этому пути имя файла 
input4 = browser.find_element(By.ID, 'file')
input4.send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
time.sleep(10)