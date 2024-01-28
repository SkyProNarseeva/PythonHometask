from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://uitestingplayground.com/textinput")
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt) 

driver.quit()