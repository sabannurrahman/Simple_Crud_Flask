import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
# open app flask
driver.get("http://127.0.0.1:5000/")
driver.maximize_window()
driver.find_element(By.ID, "login_app").click()
# login to admin
driver.find_element(By.NAME, "username").send_keys("saban123" )
driver.find_element(By.NAME, "password").send_keys("123" )
# stop 2 second
time.sleep(2)
# click login
driver.find_element(By.ID, "login").click()
time.sleep(2)

# click menu Item
driver.find_element(By.ID, "user_menu").click()

# click modal new item
driver.find_element(By.ID, "btn-delete").click()
time.sleep(1)
# click menu Item
driver.find_element(By.ID, "btn_del").click()

time.sleep(4)
# close
driver.close()