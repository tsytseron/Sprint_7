import allure
import pytest
import requests
from data import API_Data

class TestCreateOrder:
    personal_data = API_Data.personal_data
    @pytest.mark.parametrize(
        "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color", personal_data)
    @allure.title('Когда создаёшь заказ, то: можно указать один из цветов, оба цвета, совсем не указывать цвет ')
    @allure.description('Заказ успешно создан')
    def test_create_order_with_color(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate,
                                     comment, color):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [color],
        }
        response = requests.post(API_Data.CREATING_ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.text
