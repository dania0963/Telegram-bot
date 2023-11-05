import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
# options = Options()
# options.add_experimental_option("detach", True)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.get("https://my.syriatel.sy/index.php?new=1")
driver.find_element(By.ID, "SigninBut").click()
# # loginBtn = driver.find_element(By.CLASS_NAME, "mw-parser-output")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.NAME, "Username"))).send_keys('0984096261')
# driver.find_element(By.NAME, "Username").send_keys("Ahmaddhmidiy1999")
#  # find password input field and insert password as well
driver.find_element(By.NAME, "Password").send_keys("ee123456789")
# # click login button
driver.find_element(By.ID, "Signin").click()
time.sleep(4)
driver.get("https://my.syriatel.sy/history.php")
# wait = WebDriverWait(driver, 10)
# d=driver.find_element(By.CLASS_NAME,"sidebar-fixed")
# list=d.find_elements(By.XPATH,"*")
# ActionChains(driver).move_to_element(list[5].find_element(By.CLASS_NAME,"toggle-subnav")).perform()
# wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable(list[5].find_element(By.CLASS_NAME,"toggle-subnav"))).click()
#wait.until(EC.element_to_be_clickable(list[5].find_element(By.CLASS_NAME,"subnav-menu").find_element(By.TAG_NAME,"a"))).click()
# driver.get("https://my.syriatel.sy/history.php")
time.sleep(5)
driver.find_element(By.XPATH,'//a[@href="#menu1"]').click()
time.sleep(10)
element=driver.find_element(By.ID,"history1_paginate")
element.find_elements(By.TAG_NAME,"a")[-2].click()
table=driver.find_elements(By.XPATH,"//*[@id='history1']/tbody/tr")
for row in table:
    str=row.text.split(" ")
    str1=str[0]
    str2=str[8]
    print(str1,str2)

# #ActionChains(driver).move_to_element(driver.find_elements(By.TAG_NAME,'a')).perform()

print("done", )
