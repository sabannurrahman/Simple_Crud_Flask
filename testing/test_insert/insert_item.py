import os
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

# click menu Item
driver.find_element(By.ID, "item_menu").click()

# click modal new item
driver.find_element(By.ID, "new_item").click()
time.sleep(1)
# create new item
driver.find_element(By.NAME, "name_item").send_keys("sepatu Putih Baru")
driver.find_element(By.NAME, "price").send_keys("50000" )
driver.find_element(By.NAME, "stok2").send_keys("50" )
x = driver.find_element(By.NAME, "unit")
select = Select(x)
select.select_by_index(2)

upload_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "image/1.jpg"))

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(upload_file)

driver.find_element(By.NAME, "descrip").send_keys("Sepatu dengan kualitas nomor satu" )

time.sleep(2)
# click menu Item
driver.find_element(By.ID, "submit_iten").click()

time.sleep(5)
# close
driver.close()