#!/usr/bin/env python3

import sys
import os
import importlib
from src.logger import Logger
from src.validators import Validators
from providers.base_provider import BaseProvider
from src.exceptions import *
import urllib.request


class DdnsUpdater:

    PROVIDERS_DIR = 'providers'

    def __init__(self):
        self.logger = Logger()
        self.validators = Validators()

    def update(self, url: str, ip: str):
        url_formatted = url.replace('%<ip>%', ip)
        response = urllib.request.urlopen(url_formatted).read()
        print(response.decode('utf-8'))
        # response_array = json.loads(response.decode('utf-8'))
        # print(response_array['Success'])

    def main(self, argv=None):
        if argv is None:
            argv = sys.argv
        if len(argv) < 2:
            self.logger.log_msg("Usage: %s <ip_provider> <update_url> [<debug>] [ARGUMENTS...]" % argv[0])
            return 1

        ip_provider = argv[1]
        script = DdnsUpdater.PROVIDERS_DIR + '/' + ip_provider + '/' + ip_provider + '.py'
        if not os.path.exists(script):
            self.logger.log_msg("Script %s not found." % script)
            return 1

        module = importlib.import_module('providers.%s.%s' % (ip_provider, ip_provider))
        try:
            class_ = getattr(module, ip_provider.title() + 'Provider')
        except AttributeError:
            self.logger.log_msg("Class %s is not defined in %s." % (ip_provider.title(), script))
            return 1

        debug = argv[3] if len(argv) > 3 else 0
        if not self.validators.is_number(debug):
            self.logger.log_msg("Usage: %s <ip_provider> <update_url> [<debug>] [ARGUMENTS...]" % argv[0])
            return 1

        provider = class_(self.logger, int(debug))  # type: BaseProvider
        try:
            ip = provider.get_ip(argv)
        except InvalidProviderArguments as e:
            self.logger.log_msg(str(e))
            return 1
        if not ip or not self.validators.is_ip(ip):
            self.logger.log_msg('Value "%s" is not correct form of IP address' % ip)
            return 1

        update_url = argv[2]
        self.update(update_url, ip)
        return 0


if __name__ == "__main__":
    updater = DdnsUpdater()
    sys.exit(updater.main())
