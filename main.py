import os
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

load_dotenv()

base_url = os.getenv('URL')
token=os.getenv('TOKEN')
expiry_time=os.getenv('EXPIRY_TIME')
user=os.getenv('USER')

driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"))

driver.get(f"{base_url}/login")
driver.execute_script("localStorage.setItem('lang', 'en');")
driver.execute_script(f"localStorage.setItem('token','{token}');")
driver.execute_script(f"localStorage.setItem('expiry_time','{expiry_time}');")
driver.execute_script(f"localStorage.setItem('user','{user}');")
print("Please log in manually. The script will wait for you to log in...")

# Wait for 30 seconds after user logs in
time.sleep(10)

# Navigate to the next page after the wait
print("======> xxxxxx <===========")
driver.get(f"{base_url}/license/ps/license-form/NEW")

time.sleep(10)

# Quit the driver
driver.quit()
