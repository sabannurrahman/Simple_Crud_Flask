import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
# open app flask
driver.get("http://127.0.0.1:5000/")

# username and password FALSE
# find elemnet by name
driver.find_element(By.NAME, "username").send_keys("saban12" )
driver.find_element(By.NAME, "password").send_keys("12" )
# stop 2 second
time.sleep(1)
# click login
driver.find_element(By.ID, "login").click()
time.sleep(3)

# username FALSE and password TRUE
# find elemnet by name
driver.find_element(By.NAME, "username").send_keys("saban12" )
driver.find_element(By.NAME, "password").send_keys("123" )
# stop 2 second
time.sleep(1)
# click login
driver.find_element(By.ID, "login").click()
time.sleep(3)

# username TRUE and password FALSE
# find elemnet by name
driver.find_element(By.NAME, "username").send_keys("saban123" )
driver.find_element(By.NAME, "password").send_keys("12" )
# stop 2 second
time.sleep(1)
# click login
driver.find_element(By.ID, "login").click()
time.sleep(3)

# username and password required
# find elemnet by name
driver.find_element(By.NAME, "username").send_keys("" )
driver.find_element(By.NAME, "password").send_keys("" )
# stop 2 second
time.sleep(1)
# click login
driver.find_element(By.ID, "login").click()
time.sleep(3)

# close
driver.close()