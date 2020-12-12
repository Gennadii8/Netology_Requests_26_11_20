import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        HEADERS = {"Authorization": "OAuth "}

        resp1 = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                             params={"path": "/file.txt", "overwrite": "true"},
                             headers=HEADERS)

        resp1.raise_for_status()
        result1 = resp1.json()
        # pprint(result1)
        href = result1["href"]

        with open(file_path, "r") as f:
            resp2 = requests.put(href, files={"file": f})

        resp2.raise_for_status()

        return print('Загрузка прошла успешно')


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload(r'c:\my_folder\file.txt')







