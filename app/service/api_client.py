# app/service/api_client.py
import requests


class APIClient:
    BASE_URL = "http://127.0.0.1:8080/api/v1"  # 실제 API 엔드포인트로 대체

    def __init__(self, access_token=None, refresh_token=None):
        self.access_token = access_token
        self.refresh_token = refresh_token

    def get_headers(self):
        headers = {}
        if self.access_token:
            headers["Authorization"] = self.access_token
        if self.refresh_token:
            headers["Refresh"] = self.refresh_token
        return headers

    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.get_headers()
        response = requests.get(url, params=params, headers=headers)
        print(response.text)
        response.raise_for_status()
        if response.text.strip():
            return response.json()
        else:
            return {}

    def post(self, endpoint, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        if response.text.strip():
            return response.json()
        else:
            return {}

    def put(self, endpoint, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.get_headers()
        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        if response.text.strip():
            return response.json()
        else:
            return {}

    def delete(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.get_headers()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        if response.text.strip():
            return response.json()
        else:
            return {}

    def login(self, username, password):
        url = "http://127.0.0.1:8080/login"
        response = requests.post(url, json={"username": username, "password": password})
        print(response.text)
        response.raise_for_status()
        data = response.json()
        headers = response.headers
        self.access_token = headers.get("Authorization")
        self.refresh_token = headers.get("Refresh")
        return data
