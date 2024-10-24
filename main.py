import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.util.generate import generate_company_name

load_dotenv()

base_url = os.getenv('URL')
token = os.getenv('TOKEN')
expiry_time = os.getenv('EXPIRY_TIME')
user = os.getenv('USER')

driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"))

try:
    driver.get(f"{base_url}/login")
    driver.execute_script("localStorage.setItem('lang', 'en');")
    driver.execute_script(f"localStorage.setItem('token', '{token}');")
    driver.execute_script(f"localStorage.setItem('expiry_time', '{expiry_time}');")
    driver.execute_script(f"localStorage.setItem('user', '{user}');")
    print("Please log in manually. The script will wait for you to log in...")

    time.sleep(1)

    print("======> Open new route <===========")
    driver.get(f"{base_url}/license/ps/license-form/NEW")

    # Wait until the first checkbox is present and click it
    checkbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'mat-checkbox-5-input'))
    )
    checkbox.click()
    print('First checkbox clicked!')

    # Enter random number into the input field
    input_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@formcontrolname="mortgage_capital"]'))
    )
    input_field.clear()
    random_number = random.randint(300_000_001, 1_000_000_000)
    input_field.send_keys(f'{random_number:,}')
    print(f'Random number entered: {random_number:,}')

    # Click the second checkbox
    second_checkbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-checkbox-1-input"]'))
    )
    second_checkbox.click()
    print('Second checkbox clicked!')

    # Click the "Next" button
    next_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'mat-raised-button') and contains(., 'Next')]"))
    )
    next_button.click()
    print('Next button clicked!')

    # Fill the form after clicking Next
    print("Filling the form...")

    # Fill Company Registration Code
    registration_code_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, 'camdx_reg_code'))
    )
    registration_code_input.send_keys('12345678')  # Replace with actual code

    data = generate_company_name()
    # Fill Business Name (Khmer)
    business_name_kh_input = driver.find_element(By.ID, 'business_name_kh')
    business_name_kh_input.send_keys(data['khmer'])

    # Fill Business Name (English)
    business_name_en_input = driver.find_element(By.ID, 'business_name_en')
    business_name_en_input.send_keys(data['english'])  # Replace with actual name

    # Fill Province/Capital City
    province_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'company_province_dropdownMenuButton'))
    )
    province_button.click()

    province_dropdown = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'dropdown-menu'))
    )

    province_item = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dropdown-menu")]//p[text()="Phnom Penh"]'))
    )
    province_item.click()
    print('Province "Phnom Penh" selected!')

    # Fill District/Khan
    district_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'company_district_dropdownMenuButton'))
    )
    district_button.click()

    district_item = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="dropdown-menu"]//p'))
    )
    district_item.click()

    # Fill Commune/Sangkat
    commune_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'company_commune_dropdownMenuButton'))
    )
    commune_button.click()

    commune_item = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="dropdown-menu"]//p'))
    )
    commune_item.click()

    # Fill Village
    village_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'company_village_dropdownMenuButton'))
    )
    village_button.click()

    village_item = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="dropdown-menu"]//p'))
    )
    village_item.click()

    # Fill Street
    street_input = driver.find_element(By.ID, 'street_number')
    street_input.send_keys('123 Main St')  # Replace with actual street

    # Fill House/Building Number
    house_input = driver.find_element(By.ID, 'house_number')
    house_input.send_keys('456')  # Replace with actual number

    # Fill Telephone
    telephone_input = driver.find_element(By.ID, 'phone')
    telephone_input.send_keys('+855 23 456 789')  # Replace with actual telephone number

    # Fill Email
    email_input = driver.find_element(By.ID, 'contact.email')
    email_input.send_keys('example@example.com')  # Replace with actual email

    print("Form filled successfully!")

    time.sleep(10)  # Wait to see the results

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
