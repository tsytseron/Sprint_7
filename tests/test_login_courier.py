import allure
import requests
from data import API_Data

class TestLoginCourier:
    @allure.title('Для авторизации нужно передать все обязательные поля')
    @allure.description('Курьер успешно авторизован')
    def test_create_courier(self, create_courier):
        resp = requests.post(API_Data.LOGIN_COURIER, data=create_courier)
        assert resp.status_code == 200 and 'id' in resp.text

    @allure.title('Нельзя авторизоваться без логина')
    @allure.description('Недостаточно данных для входа')
    def test_authorization_without_login(self, generated_courier_data):
        requests.post(API_Data.CREATING_COURIER, data=generated_courier_data)
        generated_courier_data['login'] = ''
        resp = requests.post(API_Data.LOGIN_COURIER, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == API_Data.LOG_WITHOUT_LOGIN_PASSWORD

    @allure.title('Нельзя авторизоваться без пароля')
    @allure.description('Недостаточно данных для входа')
    def test_authorization_without_password(self, generated_courier_data):
        requests.post(API_Data.CREATING_COURIER, data=generated_courier_data)
        generated_courier_data['password'] = ''
        resp = requests.post(API_Data.LOGIN_COURIER, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == API_Data.LOG_WITHOUT_LOGIN_PASSWORD

    @allure.title('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Этот логин уже используется')
    def test_authorization_defunct_courier(self, generated_courier_data):
        resp = requests.post(API_Data.LOGIN_COURIER, data=generated_courier_data)
        assert resp.status_code == 404 and resp.json()['message'] == API_Data.NON_EXISTENT_LOGIN_PASSWORD
