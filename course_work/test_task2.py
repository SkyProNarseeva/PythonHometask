import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#Откройте страницу
def test_slow_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим значение 45 в поле с id="delay"
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем на кнопки 7, +, 8, =
    button_7 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary").click()
    plus_button = driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()
    button_8 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-of-type(2)").click()
    equal_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()
   
    # Ожидание 45 секунд
    WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))

    # Проверяем, что в окне отобразится результат 15
    result_window = driver.find_element(By.CLASS_NAME, "screen").text
    assert result_window == "15"