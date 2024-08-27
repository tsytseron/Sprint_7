class API_Data:
    # URL
    SCOOTER_WEBSITE = 'https://qa-scooter.praktikum-services.ru'
    # Courier
    LOGIN_COURIER = f'{SCOOTER_WEBSITE}/api/v1/courier/login'
    CREATING_COURIER = f'{SCOOTER_WEBSITE}/api/v1/courier'
    DELETE_COURIER = f'{SCOOTER_WEBSITE}/api/v1/courier/login'
    # Orders
    RECEIVING_ORDERS = f'{SCOOTER_WEBSITE}/api/v1/orders'
    CREATING_ORDER = f'{SCOOTER_WEBSITE}/api/v1/orders'
    # Responses
    SUCCESSFUL_RESPONSE = '{"ok":true}'
    LOG_WITHOUT_LOGIN_PASSWORD = 'Недостаточно данных для входа'
    NON_EXISTENT_LOGIN_PASSWORD = 'Учетная запись не найдена'
    CREATURE_WITHOUT_LOGIN_PASSWORD = 'Недостаточно данных для создания учетной записи'
    DUPLICATE_LOGIN = 'Этот логин уже используется'
    # Customer data
    personal_data = [
        ['Леонардо', 'Васильков', 'Энергетическая улица 18', '147', '+79998889988', '4', '2024-09-01', '', 'BLACK'],
        ['Микеланджело', 'Ирис', 'бульвар Энтузиастов, 2', '146', '+79997779977', '4', '2024-09-02', '', 'GREY'],
        ['Донателло', 'Фиалкин', 'Марксистская улица, 4', '145', '+79996669966', '4', '2024-09-03', '', 'BLACK, GREY'],
        ['Рафаэль', 'Маков', 'Климентовский переулок, 14', '144', '+79995559955', '4', '2024-09-04', '', '']
    ]
