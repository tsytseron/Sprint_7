import allure
import requests
from data import API_Data

class TestOrdersList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_returned_list_orders(self):
        resp = requests.get(API_Data.RECEIVING_ORDERS)
        assert resp.status_code == 200 and 'orders' in resp.text
