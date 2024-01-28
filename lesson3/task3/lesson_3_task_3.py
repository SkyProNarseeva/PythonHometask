from address import Address
from mailing import Mailing

from_address = Address("123123", "Moscow", "Tverskaya", "24", "12")
to_address = Address("80618", "Munich", "OdeonPlatz", "12", "167")
track = str("ERT456")
cost = int(2000.0)

mailing = Mailing(to_address, from_address, cost, track)

print(f"Отправление {mailing.track} из "
      f"Индекс: {mailing.to_address.index}, Город: {mailing.to_address.city}, Улица: {mailing.to_address.street}, Дом: {mailing.to_address.house} - Квартира: {mailing.to_address.apartment} "
      f"в Индекс: {mailing.from_address.index}, Город: {mailing.from_address.city}, Улица: {mailing.from_address.street}, Дом: {mailing.from_address.house} - Квартира: {mailing.from_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")

