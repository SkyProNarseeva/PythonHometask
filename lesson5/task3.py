from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Google Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for x in range(0, 5):
    add_element_button = chrome_driver.find_element(By.CSS_SELECTOR, "button")
    add_element_button.click()
button_delete = chrome_driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(button_delete))

# Mozilla FireFox
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(0, 5):
    add_element_button = firefox_driver.find_element(By.CSS_SELECTOR, "button")
    add_element_button.click()
button_delete = firefox_driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(button_delete))
