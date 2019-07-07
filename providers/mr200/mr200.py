#!/usr/bin/env python3

import os
import sys
from providers.base_provider import BaseProvider
from src.exceptions import *
from src.logger import Logger
from src.browser import Browser


class Mr200Provider(BaseProvider):

    def __init__(self, logger: Logger, debug: int):
        super().__init__(logger, debug)
        self.browser = Browser()
        if not os.path.exists(Logger.SCREENSHOT_DIR + "/mr200"):
            os.makedirs(Logger.SCREENSHOT_DIR + "/mr200")

    def get_ip(self, argv=None) -> str:
        if argv is None:
            argv = sys.argv
        if len(argv) < 6:
            raise InvalidProviderArguments("Usage: %s <ip_provider> <update_url> <debug> <admin_url> <admin_password>" % argv[0])

        url = str(argv[4])
        password = str(argv[5])

        return self.run(url, password)

    def run(self, url: str, password: str) -> str:
        try:
            self.login(url, password)
            self.advanced_page()
            return self.read_ipv4()
        except Exception as e:
            self.logger.log_msg(str(e))
            self.browser.save_screenshot(Logger.SCREENSHOT_DIR + "/mr200/exception.png")
            raise e
        finally:
            self.browser.quit()

    def login(self, url: str, password: str):
        self.logger.log_msg("Open %s..." % url)
        self.browser.get(url)
        if self.debug:
            self.browser.save_screenshot(Logger.SCREENSHOT_DIR + "/mr200/debug1.png")

        self.logger.log_msg("Login...")
        ele_pwd = self.browser.find_element_by_id("pcPassword")
        ele_pwd.send_keys(password)
        self.browser.find_element_by_id("login-btn").click()
        # form = self.browser.find_element_by_id("clogs")
        # form.submit()
        if self.debug:
            self.browser.save_screenshot(Logger.SCREENSHOT_DIR + "/mr200/debug2.png")

    def advanced_page(self):
        self.logger.log_msg("Opening Advanced page....")
        self.browser.find_element_by_id("advanced").click()
        if self.debug > 1:
            self.browser.save_screenshot(Logger.SCREENSHOT_DIR + "/mr200/advanced.png")

    def read_ipv4(self) -> str:
        self.logger.log_msg("Getting the IP address....")
        self.browser.implicitly_wait(10)
        return self.browser.find_element_by_id("IPV4").get_attribute("value")
