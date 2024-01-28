import pytest
from selenium import webdriver

from formPage import Form
from calculatorPage import Calculator
from shopPage import Shop


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form(driver):
   
    form = Form(driver) 
    form.fill_in_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")

    zip_code_field = form.zip_code_field_verify()
    assert "alert-danger" in zip_code_field.get_attribute("class")

    other_fields = form.other_fields_verify()
    for field in other_fields:
        assert "alert-success" in field.get_attribute("class")

def test_calculator(driver):

    test_calculator = Calculator(driver)
    test_calculator.delay("45")
    test_calculator.press_buttons('7', '+', '8', '=')
    result_window = test_calculator.result_window()

    assert result_window.text == "15"

def test_shop(driver):

    test_shop = Shop(driver)
    test_shop.login('standard_user', 'secret_sauce')
    test_shop.add_goods()
    test_shop.go_to_cart()
    test_shop.do_checkout()
    test_shop.fill_in_form("Anna", "Narseeva", "81669")
    total = test_shop.verify_total_sum()

    assert total == 'Total: $58.29'