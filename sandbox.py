from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome_driver_path = "/home/lethisa/Documents/development/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

chrome_driver_path = Service("/home/lethisa/Documents/development/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

# driver.get("https://www.amazon.com")

# driver.get("https://www.amazon.com/dp/B004S9RR5U/ref=sbl_dpx_kitchen-electric-cookware_B08QN98Y6M_0")
# price = driver.find_element(By.ID, "price_inside_buybox")
# print(price.text)

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar)
print(search_bar.get_attribute("placeholder"))

driver.close()
driver.quit()
