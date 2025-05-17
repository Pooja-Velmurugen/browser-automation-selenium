from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/automation-practice-form")

driver.maximize_window()

driver.find_element(By.ID, "firstName").send_keys("Pooja")
driver.find_element(By.ID, "lastName").send_keys("V")
driver.find_element(By.ID, "userEmail").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
driver.find_element(By.ID, "userNumber").send_keys(9876543210)
time.sleep(2)
date_input = driver.find_element(By.ID, "dateOfBirthInput")
driver.execute_script("arguments[0].value = '';", date_input)  # Clear the field
driver.execute_script("arguments[0].value = '04 Dec 2005';", date_input)
date_input.send_keys("\n")
time.sleep(2)
driver.find_element(By.ID, "subjectsInput").send_keys("practiceselenium")
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']").click()
upload_input = driver.find_element(By.ID, "uploadPicture")
upload_input.send_keys(r"C:/Users/pooja/Downloads/shinchan.jpeg")
time.sleep(2)
driver.find_element(By.ID, "currentAddress").send_keys("chennai,tamilnadu")
state_dropdown = driver.find_element(By.ID, "react-select-3-input")
state_dropdown.send_keys("NCR")
state_dropdown.send_keys("\n")
time.sleep(2)
city_dropdown = driver.find_element(By.ID, "react-select-4-input")
city_dropdown.send_keys("Delhi")
city_dropdown.send_keys("\n")
time.sleep(5)
driver.find_element(By.ID, "submit").click()

time.sleep(20)

driver.quit()
