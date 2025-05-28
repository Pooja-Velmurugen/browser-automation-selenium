from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://10fastfingers.com/typing-test/english")

driver.maximize_window()

input_field = driver.find_element(By.ID , "inputfield")

while True:
    try:
        finding_word = driver.find_element(By.CLASS_NAME, "highlight").text
        input_field.send_keys(finding_word + " ")
        time.sleep(0.5)
    except:
        print("game over")
        break    
    

time.sleep(5)
driver.quit()