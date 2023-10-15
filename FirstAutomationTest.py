import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path= "C:\\browserdrivers\chromedriver.exe")
#providing browserdriver path; We do not need to update it manually by using webdriver manager.
driver.get("https://www.vcdoctor.com/")   #url of the website
time.sleep(10)
print(driver.title)  #print the title of the website
driver.maximize_window()  #To maximize the window size
driver.close()  #close the tab only


