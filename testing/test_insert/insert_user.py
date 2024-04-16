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

# login to admin
driver.find_element(By.NAME, "username").send_keys("saban123" )
driver.find_element(By.NAME, "password").send_keys("123" )
# stop 2 second
time.sleep(2)
# click login
driver.find_element(By.ID, "login").click()
time.sleep(2)

# click menu User
driver.find_element(By.ID, "user_menu").click()

# click modal new user
driver.find_element(By.ID, "new_user").click()
time.sleep(1)
# create new item
driver.find_element(By.NAME, "name_user").send_keys("Saban Nurrahman")
driver.find_element(By.NAME, "username").send_keys("saban12345" )
driver.find_element(By.NAME, "phone_number").send_keys("08223495232" )
x = driver.find_element(By.NAME, "position")
select = Select(x)
select.select_by_index(1)
driver.find_element(By.NAME, "password").send_keys("123" )
driver.find_element(By.NAME, "pass_match").send_keys("123" )
driver.find_element(By.NAME, "address").send_keys("Pancoran Jakarta Selatan" )

time.sleep(2)
# click menu Item
driver.find_element(By.ID, "submit_create_user").click()

time.sleep(5)
# close
driver.close()