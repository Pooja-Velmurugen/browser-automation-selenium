from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  
driver.get("https://play2048.co")

time.sleep(2)

game_area = driver.find_element(By.TAG_NAME, "body")

moves = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]

try:
    while True:
        for move in moves:
            game_area.send_keys(move)
            time.sleep(0.1)  

except KeyboardInterrupt:
    print("Automation stopped by user.")
    driver.quit()