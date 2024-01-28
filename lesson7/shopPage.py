from selenium.webdriver.common.by import By

class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def login(self, user_name, password):
        #Логин 
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def add_goods(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        #Добавление товаров в корзину
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        #Переход в корзину
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    def do_checkout(self):
        #Выполнить сheckout.
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def fill_in_form(self, first_name, last_name, index):
        #Заполните форму:
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(index)
        
        #Нажмите кнопку Continue.
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def verify_total_sum(self):
        #Прочитайте со страницы итоговую стоимость
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        