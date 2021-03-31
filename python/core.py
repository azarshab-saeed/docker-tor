import time

import requests
from fake_useragent import UserAgent
from rest_framework import status
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from stem import Signal
from stem.control import Controller
from pythonping import ping
import re


class TorClient:
    options = webdriver.ChromeOptions()

    ua = UserAgent(use_cache_server=False, verify_ssl=False)
    # headers = requests.utils.default_headers()

    def __init__(self):
        self.PROXY = f"socks5://{self.get_tor_container_ip()}:9050"
        self.options.add_argument('--proxy-server=%s' % self.PROXY)
        #self.options.add_argument('--no-sandbox')
        self.options.add_argument(f'user-agent={self._get_ua()}')
        self.driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME, options=self.options)
        self.driver.set_window_position(1024, 1024, windowHandle='current')
        self.driver.set_window_size(1920, 1080)

    def get(self, url):
        self.rotate()
        response = Response()

        try:
            self.driver.get(url)
            time.sleep(5)
            response.status_code = status.HTTP_200_OK
            response.content = self.driver.page_source

        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response.content = str(e)

        return response

    def _get_ua(self):
        return self.ua.random

    def get_public_ip(self):
        proxies = {
            "http": self.PROXY,
            "https": self.PROXY,
        }

        return requests.get("https://api.ipify.org?format=json", proxies=proxies).json()['ip']

    def get_tor_container_ip(self):
        return re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(ping("tor")))[0]

    def rotate(self):
        with Controller.from_port(address=f"{self.get_tor_container_ip()}", port=9051) as controller:
            controller.authenticate(password="bonjour")
            controller.signal(Signal.NEWNYM)
            time.sleep(controller.get_newnym_wait())
        return
