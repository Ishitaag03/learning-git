import time

from selenium import  webdriver
from  selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\browserdrivers\chromedriver.exe")
driver.get("https://app.vcdoctor.com/Account/PatientRegistrations")

#1 select by visible text
element = Select(driver.find_element(By.ID, "select2-CountryCode-container"))
drp= (element)
time.sleep(5)
drp.select_by_visible_text("(+1) United States")
driver.quit()