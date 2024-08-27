import allure
import requests
from data import API_Data

class TestCreatingCourier:
    @allure.title('Чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @allure.description('Курьер успешно создан')
    def test_create_courier(self, generated_courier_data):
        resp = requests.post(API_Data.CREATING_COURIER, data=generated_courier_data)
        assert resp.status_code == 201 and resp.text == API_Data.SUCCESSFUL_RESPONSE

    @allure.title('Нельзя создать курьера без логина')
    @allure.description('Недостаточно данных для создания учетной записи')
    def test_create_courier_without_login(self, generated_courier_data):
        generated_courier_data['login'] = ''
        resp = requests.post(API_Data.CREATING_COURIER, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == API_Data.CREATURE_WITHOUT_LOGIN_PASSWORD

    @allure.title('Нельзя создать курьера без пароля')
    @allure.description('Недостаточно данных для создания учетной записи')
    def test_create_courier_without_password(self, generated_courier_data):
        generated_courier_data['password'] = ''
        resp = requests.post(API_Data.CREATING_COURIER, data=generated_courier_data)
        assert resp.status_code == 400 and resp.json()['message'] == API_Data.CREATURE_WITHOUT_LOGIN_PASSWORD

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('Этот логин уже используется')
    def test_cannot_create_duplicate_courier(self, generated_courier_data):
        requests.post(API_Data.CREATING_COURIER, data=generated_courier_data)
        duplicate_courier = requests.post(API_Data.CREATING_COURIER, data=generated_courier_data)
        assert duplicate_courier.status_code == 409 and duplicate_courier.json()['message'] == API_Data.DUPLICATE_LOGIN
