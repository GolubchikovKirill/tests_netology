import unittest
from unittest.mock import patch, Mock
import requests

# Функция для создания папки на Яндекс.Диске
def create_folder(folder_name, auth_token):
    url = f'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Authorization': f'OAuth {auth_token}'
    }
    params = {
        'path': folder_name
    }
    response = requests.put(url, headers=headers, params=params)
    return response

class TestYandexDiskAPI(unittest.TestCase):

    @patch('requests.put')
    def test_create_folder_success(self, mock_put):
        # Мокаем успешный ответ от API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"path": "/test_folder"}
        mock_put.return_value = mock_response

        # Параметры для теста
        folder_name = "test_folder"
        auth_token = "valid_token"

        # Создание папки
        response = create_folder(folder_name, auth_token)

        # Проверяем, что код ответа - 200
        self.assertEqual(response.status_code, 200)

        # Проверяем, что папка появилась в списке файлов
        self.assertEqual(response.json()["path"], "/test_folder")

    @patch('requests.put')
    def test_create_folder_bad_request(self, mock_put):
        # Мокаем ответ с ошибкой 400
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Invalid request"}
        mock_put.return_value = mock_response

        # Параметры для теста
        folder_name = "test_folder"
        auth_token = "valid_token"

        # Попытка создать папку
        response = create_folder(folder_name, auth_token)

        # Проверяем, что код ответа - 400
        self.assertEqual(response.status_code, 400)

        # Проверяем, что ошибка в ответе
        self.assertEqual(response.json()["error"], "Invalid request")

    @patch('requests.put')
    def test_create_folder_unauthorized(self, mock_put):
        # Мокаем ответ с ошибкой 401
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"error": "Unauthorized"}
        mock_put.return_value = mock_response

        # Параметры для теста
        folder_name = "test_folder"
        auth_token = "invalid_token"  # Некорректный токен

        # Попытка создать папку
        response = create_folder(folder_name, auth_token)

        # Проверяем, что код ответа - 401
        self.assertEqual(response.status_code, 401)

        # Проверяем, что ошибка в ответе
        self.assertEqual(response.json()["error"], "Unauthorized")

    @patch('requests.put')
    def test_create_folder_server_error(self, mock_put):
        # Мокаем ответ с ошибкой 500
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"error": "Internal server error"}
        mock_put.return_value = mock_response

        # Параметры для теста
        folder_name = "test_folder"
        auth_token = "valid_token"

        # Попытка создать папку
        response = create_folder(folder_name, auth_token)

        # Проверяем, что код ответа - 500
        self.assertEqual(response.status_code, 500)

        # Проверяем, что ошибка в ответе
        self.assertEqual(response.json()["error"], "Internal server error")

if __name__ == "__main__":
    unittest.main()