# Test Case #
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
serv_obj=Service("D:\Browser_Drivers\chromedriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://tutorialsninja.com/demo/")
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.ID,"password").send_keys("admin123")
# driver.find_element(By.ID,"btnLogin").click()

act_title=driver.title
# exp_title="OrangeHRM"
exp_title="Your Store"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
# driver.close()
'''

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
serv_obj=Service("D:\Browser_Drivers\geckodriver\geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)
driver.get("https://tutorialsninja.com/demo/")

act_title=driver.title
exp_title="Your Store"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

