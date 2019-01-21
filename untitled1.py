# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:58:18 2019

@author: Rohan Joseph
"""
from selenium import webdriver

        
check1=["-"]
        
check2=["A"]                 

absent=[]
unmark=[]
   
    #______________________________ google chrome khjolne wala code _____________________________   

driver=webdriver.Chrome("C:\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://eduserve.karunya.edu/Login.aspx?ReturnUrl=%2f")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id("mainContent_Login1_UserName").send_keys("ur16cs209")
driver.find_element_by_id("mainContent_Login1_Password").send_keys("nishu1211")
driver.find_element_by_id("mainContent_Login1_LoginButton").click()
driver.get("https://eduserve.karunya.edu/Student/AttSummary.aspx")
driver.find_element_by_id("mainContent_DDLACADEMICTERM").send_keys("2018-19 Even Semester")
driver.save_screenshot("rohanatt.png")
x=driver.find_element_by_xpath('//*[@id="ctl00_mainContent_grdData_ctl00__0"]').text
a=driver.find_element_by_xpath('//*[@id="mainContent_UCStudentAttendance_LBLTOTALDAYS"]').text
print("------------------------")
print(x)
y=x.split();
print(y)

date=""



for f in range(3):
    date=date+y[f]
    date=date+" "
print("the current date is"+" "+date)

   
for f,k in enumerate(y):
    
    if k in check1:
        
        unmark.append(f-2)
        
    if k in check2:
        absent.append(f-2)
        


print("your unmarked in: ",unmark)
print(absent)    
print("total attendance is:",a)
         #way to sms wala code
driver.get("http://site21.way2sms.com/content/index.html")
driver.find_element_by_id("mobileNo").send_keys("9515373965")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div[2]/button').click()
driver.find_element_by_id("mobile").send_keys("8072137030")
driver.find_element_by_id("message").send_keys(str(unmark))
driver.find_element_by_id("sendButton").click()


