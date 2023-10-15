#Automation for login and editing an organization
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import *
from selenium.webdriver.chrome.service import Service

serv_ob = Service("C:\browserdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_ob)
driver.get("https://www.vcdoctor.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".helpsupport").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//a[@class='button2 mt-0 requestbtn'])[1]").click()
time.sleep(1)
def login_page():
 select = Select(driver.find_element(By.ID, "CountryCode"))
 time.sleep(1)
# select by visible text
 select.select_by_value("672")
time.sleep(5)


 # element1 = driver.find_elements(By.CLASS_NAME, "select2-selection__rendered") #for country code
 # targeted_text="(+91) India "
 # matching_element = None
 # for element in element1:
 #        if element.text == targeted_text:
 #            matching_element = element
 #            break
  # element1[0].click()
 # driver.find_elements(By.CLASS_NAME, "select2-selection__rendered") #for the username

driver.find_element(By.NAME, "UserName").send_keys("2222222222") #for the username
time.sleep(1)
driver.find_element(By.NAME, "Password").send_keys("gfp2fJ$g2UV3")  #for password
time.sleep(1)
driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click() #for clicking the login button
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Yes']").click()
time.sleep(1.5)

login_page()
# wait = WebDriverWait(driver, 10) #another way of clicking login button
# element2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Yes']")))
# # Click the element
# element2.click()
def manage_organization():
 driver.find_element(By.LINK_TEXT, "Manage Organizations").click() #clicking on manage organizations
 time.sleep(1.5)
 driver.find_element(By.LINK_TEXT, "Edit").click() #clicking on edit button
 time.sleep(1.5)
manage_organization()

def edit_form():
 driver.find_element(By.NAME, "FirstName").clear() #clearing the field
 time.sleep(1.5)
 driver.find_element(By.NAME, "FirstName").send_keys("Harper")  #entering desired data in first name
 time.sleep(1.5)
 driver.find_element(By.NAME, "MiddleName").clear()  #clearing the field
 time.sleep(1.5)
 driver.find_element(By.NAME, "MiddleName").send_keys("S")   #entering desired data in middle name
 time.sleep(1.5)
 driver.find_element(By.NAME, "LastName").clear()
 time.sleep(1.5)
 driver.find_element(By.NAME, "LastName").send_keys("Garcia")
 time.sleep(1.5)
 driver.find_element(By.NAME, "Email").clear()
 time.sleep(1.5)
 driver.find_element(By.NAME, "Email").send_keys("Garcia@yopmail.com")
 time.sleep(1.5)
 driver.find_element(By.NAME, "Designation").clear()
 time.sleep(1.5)
 driver.find_element(By.NAME, "Designation").send_keys("Physician and Organization Administrator")
 time.sleep(5)

 # Date picker code start
 driver.find_element(By.CSS_SELECTOR, ".add-on.calbox").click()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "div[class='datepicker-days'] th[class='switch']").click()
 driver.find_element(By.CSS_SELECTOR, "div[class='datepicker-months'] th[class='switch']").click()
 time.sleep(1)
 driver.find_element(By.XPATH, "//span[normalize-space()='1964']").click()
 time.sleep(1)
 driver.find_element(By.XPATH, "(//span[normalize-space()='Jun'])[1]").click()
 time.sleep(1)
 driver.find_element(By.XPATH,"//td[@class='day'][normalize-space()='18']").click()
 time.sleep(1)




 # driver.find_element(By.XPATH,"(//input[@id='Gender'])[2]").clear()
 driver.find_element(By.XPATH,"(//input[@id='Gender'])[1]").click()
 # driver.find_element(By.XPATH, "//div[@id='videoCallTableDiv']//form").click()
 # time.sleep(0.5)
 driver.find_element(By.NAME, "AlternateEmail").send_keys("Harper@yopmail.com")
 time.sleep(0.5)
 driver.find_element(By.CSS_SELECTOR, "#Address").send_keys("23456 Willow Creek Road, Lexington")
 time.sleep(0.5)
 driver.find_element(By.CSS_SELECTOR, "#ZipCode").send_keys("56789")
 time.sleep(0.5)
 driver.find_element(By.CSS_SELECTOR, "#CountryID").click()
 country_code = driver.find_elements(By.CSS_SELECTOR, "#CountryID")  # for country code
 targeted_text = "United States"
 matching_element = None
 for element in country_code:
    if element.text == targeted_text:
        matching_element = element
        break
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#StateID").click()
 state_id = driver.find_elements(By.CSS_SELECTOR, "#StateID") #for country code
 targeted_text="Indiana"
 matching_element = None
 for element in state_id:
        if element.text == targeted_text:
            matching_element = element
            break
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#StateID").click()
 city_id = driver.find_elements(By.CSS_SELECTOR, "#StateID") #for country code
 targeted_text="Evansville"
 matching_element = None
 for element in city_id:
        if element.text == targeted_text:
            matching_element = element
            break
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#NPI").clear()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#NPI").send_keys("123456")
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "button[type='submit'] span").click()
 time.sleep(5)
edit_form()
def basics():
 driver.find_element(By.XPATH,"//span[normalize-space()='Basics']").click()
 time.sleep(0.5)
 driver.find_element(By.NAME,"OrgName").clear()
 time.sleep(1)
 driver.find_element(By.NAME, "OrgName").send_keys("Duke University Hospital")
 time.sleep(1)
 driver.find_element(By.NAME, "SlugURL").clear()
 time.sleep(1)
 driver.find_element(By.NAME,"SlugURL").send_keys("Duke University Hospital")
 time.sleep(1)
 driver.find_element(By.NAME, "CountryID").click()
 time.sleep(1)
 country_id =driver.find_elements(By.NAME,"CountryID")
 targeted_text="United States"
 matching_element=None
 for element in country_id:
     if element.text==targeted_text:
         matching_element=element
         break
 time.sleep(1)
 driver.find_element(By.NAME,"OrgType").click()
 time.sleep(1)
 org_type=driver.find_elements(By.NAME,"OrgType")
 target_text="Hospital"
 matched_element=None
 for element in org_type:
       if element.text==target_text:
           matched_element=element
           break
 time.sleep(1)
 driver.find_element(By.NAME,"EstbYear").clear()
 time.sleep(1)
 driver.find_element(By.NAME,"EstbYear").send_keys("1856")
 time.sleep(0.5)
 driver.find_element(By.NAME,"RegNumber").clear()
 time.sleep(0.5)
 driver.find_element(By.NAME,"RegNumber").send_keys("12345678")
 time.sleep(0.5)
 driver.find_element(By.CSS_SELECTOR,".add-on.calbox").click()
 time.sleep(1)
 driver.find_element(By.XPATH,"(//td[@class='day'][normalize-space()='5'])[1]").click()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, ".add-on.calbox").click()
 time.sleep(1)
 driver.find_element(By.CLASS_NAME, "switch").click()
 time.sleep(1)
 driver.find_element(By.XPATH,"(//span[contains(text(),'Nov')])[2]").click()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, ".add-on.calbox").click()
 time.sleep(1)
 driver.find_element(By.CLASS_NAME, "switch").click()
 time.sleep(1)
 driver.find_element(By.CLASS_NAME, "switch").click()
 time.sleep(1)
 driver.find_element(By.CLASS_NAME,"next").click()
 time.sleep(1)
 driver.find_element(By.CLASS_NAME, "next").click()
 time.sleep(1)
 driver.find_element(By.XPATH,"(//span[normalize-space()='2035'])[1]").click()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#NationalIdType").click()
 time.sleep(1)
 id_type=driver.find_element(By.CSS_SELECTOR, "#NationalIdType")
 id_text="Aadhar Card Number"
 match_element=None
 for element in id_type:
     if element.text==id_text:
         matching_element=element
         break
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"#NationalIdValue").click()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"#NationalIdValue").send_keys("123456")
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"#TaxationIdType").click()
 id=driver.find_element(By.CSS_SELECTOR,"#TaxationIdType")
 ids_text="Aadhar Card Number"
 the_element=None
 for element in id:
     if element.text==ids_text:
         the_element=element
         break
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"button[type='submit'] span").click()
 time.sleep(1)
basics()

def contacts():
 driver.find_element(By.CSS_SELECTOR,"#ISDMobile").click()
 isd=driver.find_element(By.CSS_SELECTOR,"#ISDMobile")
 isd_text="1"
 isd_element=None
 for element in isd:
        if element.text==isd_text:
            isd_element=element
            break
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"#Mobile").clear()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"#Mobile").send_keys("1234567891")
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#ISDMobileSecondary").click()
 isdS = driver.find_element(By.CSS_SELECTOR, "#ISDMobileSecondary")
 isdS_text = "1"
 isdS_element = None
 for element in isdS:
     if element.text == isdS_text:
         isdS_element = element
         break
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#ISDMobileSecondary").clear()
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR, "#ISDMobileSecondary").send_keys("1234567891")
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"#Email").send_keys("Duke@yopmail.com")
 time.sleep(1)
 driver.find_element(By.CSS_SELECTOR,"#CountryID").click()
 country = driver.find_element(By.CSS_SELECTOR, "#CountryID")
 country_text = "United States"
 country_element = None
 for element in country:
  if element.text == country_text:
   country_element = element
   break
 time.sleep(1)

 driver.find_element(By.CSS_SELECTOR, "#StateID").click()
 state = driver.find_element(By.CSS_SELECTOR, "#StateID")
 state_text = "Arizona"
 state_element = None
 for element in state:
  if element.text == state_text:
   state_element = element
   break
 time.sleep(1)

 driver.find_element(By.CSS_SELECTOR, "#CityID").click()
 city = driver.find_element(By.CSS_SELECTOR, "#CityID")
 city_text = "Gilbert"
 city_element = None
 for element in city:
  if element.text == city_text:
   city_element = element
   break
 time.sleep(1)
 driver.find_element(By.CLASS_NAME,"fas fa-user-plus").click()
 time.sleep(10)
 driver.find_element(By.CSS_SELECTOR,"button[type='submit'] span").click()
contacts()
driver.close()