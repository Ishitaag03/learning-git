# Registering a patient
import select
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium import *
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import InvalidSelectorException

serv_ob = Service("C:\browserdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_ob)
driver.get("https://www.vcdoctor.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".helpsupport").click()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Patient").click()
time.sleep(10)
driver.find_element(By.XPATH, " (//select[@id='CountryCode'])[1]").click()
time.sleep(0.5)
country = driver.find_elements(By.XPATH, " (//select[@id='CountryCode'])[1]")
target_text = "(+91) India"
matching_element = None
for element in country:
    if element.text == target_text:
        matching_element = element
        break
# while True:
#     try:
# return matching_element
# raise InvalidSelectorException:
#      print("!!!! ERROR IN SELECTING THE COUNTRY !!!!")
# driver.find_element(By.CLASS_NAME, "select2-selection__rendered").click()
# time.sleep(10)
# country= driver.find_element(By.ID, "select2-CountryCode-result-aw16-1").c()
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#PhoneNumber").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#PhoneNumber").send_keys("1234567891")
time.sleep(15)
driver.find_element(By.CSS_SELECTOR, "#btnCapcha").click()
time.sleep(1)
driver.find_element(By.ID,"btnGetOTP").click()
time.sleep(15)
driver.find_element(By.ID.,"btnVerifyOTP").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@id='PresenterType'])[2]").click()
time.sleep(1)
driver.find_element(By.ID,"FirstName").send_keys("Ilana")
time.sleep(1)
driver.find_element(By.ID,"LastName").send_keys("Kocher")
time.sleep(1)
driver.find_element(By.ID,"Password").send_keys("pass@123")
time.sleep(1)
driver.find_element(By.ID,"ConfirmPassword").send_keys("pass@123")
time.sleep(1)
driver.find_element(By.ID,"Country").click()
country=driver.find_element(By.ID,"Country")
targ_text="India"
match_element=None
for element in country:
    if element.text==targ_text:
        match_element=element
        break
driver.find_element(By.ID,"State").click()
state=driver.find_element(By.ID,"State")
targ1_text="Rajasthan"
match1_element=None
for element in state:
    if element.text==targ1_text:
        match1_element=element
        break
time.sleep(1)
driver.find_element(By.ID,"CityName").send_keys("Jaipur")
time.sleep(1)
driver.find_element(By.ID,"ReferenceType").click()

driver.close()

