from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
import keyboard
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.alert import Alert
import pyautogui
from os import system
import cred
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

startTime = cred.startTime
endTime = cred.endTime
email = cred.creds[0]
password = cred.creds[1]
meetingCode = cred.meetingCode

# while current_time != (startTime):
#     now = datetime.datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print(current_time)
#     system("cls")  
# current_time == (startTime)
if True:
    webdriver.Chrome() 
    opt = Options()
    # Open With maximized Screen
    opt.add_argument("start-maximized")
    # Add Permission for Microphone , Camera and Notificaion 
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1 
    })


    driver = webdriver.Firefox(executable_path=r'chromedriver.exe')
    driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    #Email Passed
    time.sleep(3)
    emailInput = driver.find_element_by_name("identifier")
    emailInput.send_keys(email)
    time.sleep(3)
    emailInput.send_keys(Keys.RETURN)
    time.sleep(5)
  
    #password Passed 
    passInput = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    passInput.send_keys(password)
    passInput.send_keys(Keys.RETURN)

    #Open Google Meet With Your Code
    time.sleep(3)
    driver.get("https://meet.google.com/lookup/" + meetingCode)
    time.sleep(3)

    # Turn OFF  Video By Default
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()
    # Turn OFF Video By Default
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
    # Join Class
    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
    time.sleep(20)
    while current_time != endTime:
            system("cls")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)

    if current_time == endTime:
        driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div").click()






