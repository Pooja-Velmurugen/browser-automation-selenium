"""
note :Before running this program, you need to change the data in the code
      1) change the username ans the password in the username.send_keys() and password.send_keys()
      2) change the your_frnd_id in the variable chat
      3) change the time of iteration in the for loop range(n) 
         n -> no fo time u want to snd the same msg
      4) change the msg in the message variable. 
      After running wait and see magic.✨🎉
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")

time.sleep(7)  

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("Your_id or Gmain")
password.send_keys("password")
password.send_keys(Keys.RETURN)
 
time.sleep(5)
try:
    save_info_not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Not now']"))
    )
    save_info_not_now.click()
    print("closed (Save Info popup)")
except TimeoutException:
    print("not closed (Save Info popup)")

time.sleep(5)
dm_icon = driver.find_element(By.XPATH, "//a[contains(@href,'/direct/inbox')]")
dm_icon.click()
print("navigated to the msg")

try:
    notif_not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
    )
    notif_not_now.click()
    print("closed (Notification popup)")
except TimeoutException:
    print("not closed (Notification popup)")



time.sleep(5)

try:
    chat = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'your_frnd_id')]"))
    )
    chat.click()
    print("Opened chat with frnd.")
except Exception as e:
    print("Could not find the chat with frnd.")
    print(e)

try:
    # Locate the input box using its role attribute
    message_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
    )

    message = "Hello, frnd! This is an automated message."
    for i in range(20):
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
    print("Message sent successfully.")
except Exception as e:
    print("Could not send the message.")
    print(e)

time.sleep(20)
driver.quit()
