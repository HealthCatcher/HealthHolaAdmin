# app/service/api_client.py
import requests


class APIClient:
    BASE_URL = "http://127.0.0.1:8080/api/v1"  # 실제 API 엔드포인트로 대체

    def __init__(self):
        self.auth_token = "eyJhbGciOiJIUzI1NiJ9.eyJjYXRlZ29yeSI6ImFjY2VzcyIsInVzZXJuYW1lIjoic3RyaW5nIiwicm9sZSI6IlJPTEVfQURNSU4iLCJpYXQiOjE3Mzg1OTA1NjEsImV4cCI6MTczODYyNjU2MX0.fQpPv3xvhEyyLYWrdqqDoqW2xw7GfkCP1BxQeXWBNbo"
        self.refresh_token = ""

    def get_headers(self):
        headers = {}
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        if self.refresh_token:
            headers["Refresh"] = f"Bearer {self.refresh_token}"
        return headers

    def get_headers(self):
        headers = {}
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        if self.refresh_token:
            headers["Refresh"] = f"Bearer {self.refresh_token}"
        return headers

    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.get_headers()
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

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
        return response.json()

    def delete(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.get_headers()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        if response.text.strip():
            return response.json()
        else:
            return {}
