import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

# open app flask with link Item
driver.get("http://127.0.0.1:5000/Items")
driver.maximize_window()
# stop 2 second
time.sleep(2)

# open app flask with link User
driver.get("http://127.0.0.1:5000/Users")
# stop 2 second
time.sleep(2)

# open app flask with link Dashboard Admin
driver.get("http://127.0.0.1:5000/Admin_Dashboard")
# stop 2 second
time.sleep(2)

# close
driver.close()