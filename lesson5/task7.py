from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Google Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
chrome_driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода по тегу и вводим текст "1000"
input_field = chrome_driver.find_element(By.CSS_SELECTOR, "input")
input_field.send_keys("1000")

# Очищаем поле ввода
input_field.clear()

# Вводим текст "999" 
input_field.send_keys("999")


# Mozilla FireFox
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода по тегу и вводим текст "1000"
input_field = firefox_driver.find_element(By.CSS_SELECTOR, "input")
input_field.send_keys("1000")

# Очищаем поле ввода
input_field.clear()

# Вводим текст "999" 
input_field.send_keys("999")
