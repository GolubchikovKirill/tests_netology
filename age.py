def check_age(age: int):

    if age >= 18: # Введите условие для проверки возраста
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result