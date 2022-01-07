from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("/home/lethisa/Documents/development/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# article_count.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# driver.close()
# driver.quit()
