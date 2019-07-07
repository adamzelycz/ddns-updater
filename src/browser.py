#!/usr/bin/env python3

from selenium import webdriver
import os


class Browser(webdriver.Chrome):

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/74.0.3729.169 " \
                 "Chrome/74.0.3729.169 Safari/537.36 "

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        # options.add_argument("privileged")
        # options.add_argument("disable-gpu")
        options.add_argument("no-sandbox")  # need when run in docker
        options.add_argument("window-size=1200x800")
        options.add_argument("user-agent=%s" % self.USER_AGENT)
        if 'https_proxy' in os.environ:
            options.add_argument("proxy-server=" + os.environ['https_proxy'])

        super().__init__(chrome_options=options)
        self.set_page_load_timeout(60)
