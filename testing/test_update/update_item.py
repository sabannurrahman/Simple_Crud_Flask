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
driver.find_element(By.ID, "btn_update").click()
time.sleep(1)
# clear
elements_to_clear = ["name_item3", "price3", "stok3", "descript4"]
for element_name in elements_to_clear:
    driver.find_element(By.NAME, element_name).clear()
    time.sleep(1)

driver.find_element(By.NAME, "name_item3").send_keys("Sepatu Coba")
driver.find_element(By.NAME, "price3").send_keys("2000" )
driver.find_element(By.NAME, "stok3").send_keys("40" )
x = driver.find_element(By.NAME, "unit3")
select = Select(x)
select.select_by_index(1)
driver.find_element(By.NAME, "descript4").send_keys("Sepatu testing  " )

time.sleep(2)
# click menu Item
driver.find_element(By.ID, "submit_update").click()

time.sleep(4)
# close
driver.close()