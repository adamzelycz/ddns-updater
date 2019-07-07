#!/usr/bin/env python3

import sys
from providers.base_provider import BaseProvider
from src.exceptions import *


class StaticProvider(BaseProvider):

    def get_ip(self, argv=None) -> str:
        if argv is None:
            argv = sys.argv
        if len(argv) < 5:
            raise InvalidProviderArguments("Usage: %s <ip_provider> <update_url> <debug> <ip address>" % argv[0])

        ip = str(argv[4])
        return ip
