from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("/home/lethisa/Documents/development/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Lethisa")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Putri")
email = driver.find_element(By.NAME, "email")
email.send_keys("lethisaputri@cecakit.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

