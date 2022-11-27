# Non-standard naming (PascalCase) triggers the pylint-warning
# "invalid-name"; disable that for this file:
# pylint: disable=invalid-name

import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset", timeout=20) # timeout 20s

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,
            "password_confirm": password
        }

        requests.post(f"{self._base_url}/register", data=data, timeout=20)
