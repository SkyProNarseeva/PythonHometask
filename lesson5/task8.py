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
chrome_driver.get("http://the-internet.herokuapp.com/login")

# Находим поле username и вводим значение "tomsmith"
username = chrome_driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")

# Находим поле password и вводим значение "SuperSecretPassword!"
password = chrome_driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword")

# Нажимаем кнопку Login
login_button = chrome_driver.find_element(By.CSS_SELECTOR, "button.radius").click()



# Mozilla FireFox
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
firefox_driver.maximize_window()
firefox_driver.get("http://the-internet.herokuapp.com/login")

# Находим поле username и вводим значение "tomsmith"
username = chrome_driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")

# Находим поле password и вводим значение "SuperSecretPassword!"
password = chrome_driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword")

# Нажимаем кнопку Login
login_button = chrome_driver.find_element(By.CSS_SELECTOR, "button.radius").click()