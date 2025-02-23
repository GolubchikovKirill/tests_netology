def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'

    return result