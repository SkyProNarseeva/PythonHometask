from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro Max", "+491567894567"),
    Smartphone("Samsung", "Galaxy S21", "+1567894563"),
    Smartphone("Pixel", "Pixel Pro", "+79156784536"),
    Smartphone("Apple", "iPhone X", "+7915679332"),
    Smartphone("Apple", "iPhone 12", "+791568967")
]

for phone in catalog:
    print(f"Бренд телефона: {phone.brand}. Модель телефона: {phone.model}. Номер телефона: {phone.phone_number}")

    