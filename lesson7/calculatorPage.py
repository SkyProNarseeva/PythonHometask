import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
        
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Устанавливаем delay
    def delay(self, time):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(time)

    # Нажимаем на кнопки 7, +, 8, =
    def press_buttons(self, button1, button2, button3, button4):
        elements = self.driver.find_elements(By.CLASS_NAME, "btn-outline-primary")
        elements.extend(self.driver.find_elements(By.CLASS_NAME, "btn-outline-success"))
        elements.extend(self.driver.find_elements(By.CLASS_NAME, "btn-outline-warning"))
        for element in elements:
            if element.text == button1:
                element.click()
        for element in elements:
            if element.text == button2:
                element.click()
        for element in elements:
            if element.text == button3:
                element.click()
        for element in elements:
            if element.text == button4:
                element.click()

        # Ждем 45 секунд
        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))

    # Проверяем, что в окне отобразится результат 15
    def result_window(self):
        return self.driver.find_element(By.CLASS_NAME, "screen")
        

   