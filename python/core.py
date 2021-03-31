import time
import requests
from stem import Signal
from stem.control import Controller
from pythonping import ping
import re


class TorClient:
    def __init__(self):
        self.PROXY = f"socks5://{self.get_tor_container_ip()}:9050"

    def get(self, url):
        self.rotate()
        response = requests.get(url)
        return response

    def get_public_ip(self):
        proxies = {
            "http": self.PROXY,
            "https": self.PROXY,
        }

        return requests.get("https://api.ipify.org?format=json", proxies=proxies).json()['ip']

    def get_tor_container_ip(self):
        return re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(ping("tor")))[0]

    def rotate(self):
        # Rotate tor public ip
        with Controller.from_port(address=f"{self.get_tor_container_ip()}", port=9051) as controller:
            controller.authenticate(password="bonjour")
            controller.signal(Signal.NEWNYM)
            time.sleep(controller.get_newnym_wait())
        return
