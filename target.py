from selenium import webdriver
import pyautogui
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"


# Import csv file 
df = pd.read_excel (r'targetaccounts.xlsx')

for i, row in df.iterrows():	
	email = df.email
	firstname = df.firstname
	lastname = df.lastname
	password = df.password

	driver = webdriver.Chrome(PATH)
	driver.get("https://www.target.com/")
	link = driver.find_element_by_id("account")
	link.click()
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.LINK_TEXT, "Create account"))
	    )
	    element.click()
	    time.sleep(1)
	    pyautogui.typewrite(email[i])
	    pyautogui.typewrite(["tab"])
	    pyautogui.typewrite(firstname[i])
	    pyautogui.typewrite(["tab"])
	    pyautogui.typewrite(lastname[i])
	    pyautogui.typewrite(["tab"])
	    pyautogui.typewrite(["tab"])
	    pyautogui.typewrite(password[i])
	    pyautogui.press('enter')
	    pyautogui.press('enter')
	    time.sleep(1)
	    driver.quit()
	    #skipcircle = driver.find_element_by_id("circle-skip")
	    #skipcircle.click() 
	except:
	    driver.quit()
	    
