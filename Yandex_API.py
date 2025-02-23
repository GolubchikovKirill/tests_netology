import requests
import os
from dotenv import load_dotenv

load_dotenv()

YANDEX_TOKEN = os.getenv("YANDEX_TOKEN")

YANDEX_DISK_URL = "https://cloud-api.yandex.net/v1/disk/"

headers = {
    "Authorization": f"OAuth {YANDEX_TOKEN}"
}


def get_disk_info():
    response = requests.get(f"{YANDEX_DISK_URL}resources", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


def create_folder(folder_name):
    params = {
        "path": folder_name
    }
    response = requests.put(f"{YANDEX_DISK_URL}resources", headers=headers, params=params)

    if response.status_code == 201:
        print(f"Folder '{folder_name}' created successfully!")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


def upload_file(local_file_path, remote_file_path):
    upload_url = get_upload_url(remote_file_path)
    if not upload_url:
        return

    with open(local_file_path, "rb") as file:
        response = requests.put(upload_url, files={"file": file})

    if response.status_code == 201:
        print(f"File '{local_file_path}' uploaded successfully!")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


def get_upload_url(remote_file_path):
    params = {
        "path": remote_file_path
    }
    response = requests.get(f"{YANDEX_DISK_URL}resources/upload", headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("href")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def list_files(folder_name):
    params = {
        "path": folder_name
    }
    response = requests.get(f"{YANDEX_DISK_URL}resources", headers=headers, params=params)

    if response.status_code == 200:
        files = response.json().get("_embedded", {}).get("items", [])
        print(f"Files in '{folder_name}':")
        for file in files:
            print(file["name"])
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    disk_info = get_disk_info()
    print(disk_info)

    # Создание папки
    folder_name = "test_folder"
    create_folder(folder_name)

    # Загрузка файла
    local_file = "example.txt"
    remote_file = f"{folder_name}/example.txt"
    upload_file(local_file, remote_file)

    # Список файлов в папке
    list_files(folder_name)