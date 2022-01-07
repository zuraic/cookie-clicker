from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("/home/lethisa/Documents/development/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get("https://www.python.org/events/python-events/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events .event-title")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.close()
driver.quit()
