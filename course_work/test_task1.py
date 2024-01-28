import time 
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Откройте страницу
def test_forma(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
   
    # Заполните форму значениями
    driver.find_element(By.NAME, 'first-name').send_keys("Иван") 
    driver.find_element(By.NAME, 'last-name').send_keys("Петров") 
    driver.find_element(By.NAME, 'address').send_keys("Ленина, 55-3") 
    driver.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
    driver.find_element(By.NAME, 'phone').send_keys("+7985899998787")
    driver.find_element(By.NAME, 'zip-code').send_keys("")
    driver.find_element(By.NAME, 'city').send_keys("Москва")
    driver.find_element(By.NAME, 'country').send_keys("Россия")
    driver.find_element(By.NAME, 'job-position').send_keys("QA")
    driver.find_element(By.NAME, 'company').send_keys("SkyPro")
         
    # Нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, 'button').click()

    # Проверка, что поле Zip code подсвечено красным
    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    # Проверьте (assert), что остальные поля подсвечены зеленым
    other_fields = driver.find_elements(By.CLASS_NAME, "alert-success")
    for field in other_fields:
        assert "alert-success" in field.get_attribute("class")


    #еще вариант проверка цвета       
    # zip_code_color = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    # assert zip_code_color == "rgba(248, 215, 218, 1)"