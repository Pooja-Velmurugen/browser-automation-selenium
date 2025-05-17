"""
note :Before running this program, you need to change the data in the code
      1) change the frnd_name in the  search_box.send_keys()
      2) change the frnd_name in the variable frnd_chat
      3) change the time of iteration in the for loop range(n) 
         n -> no fo time u want to snd the same msg
      4) change the msg in the msg_box.send_keys() 
      After running..scan the QR code and link to ur Whatsapp and the wait and see magic.✨🎉
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe") # path of chromedriver
driver = webdriver.Chrome(service=service)
driver.get("https://web.whatsapp.com/")

#Scan the QR code within 15 seconds...

time.sleep(15)

try:
    # searching frnd
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
    )
    search_box.click()
    time.sleep(1)
    search_box.send_keys("frnd_name")
    time.sleep(2)

    # opening frnd chat 
    frnd_chat = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@title='frnd_name']")) # change the friend name
    )
    frnd_chat.click()
    print("Opened chat with frnd.")

except Exception as e:
    print("Could not find or open chat with frnd.")
    print(e)
    

msg_box = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
)
msg_box.click()
time.sleep(1)

for i in range(20): # change the msg time according to ur need 
    msg_box.send_keys("Hello, frnd! This is an automated message.")
    time.sleep(1)
    msg_box.send_keys(Keys.ENTER)   

time.sleep(40)
driver.quit()
