#!/usr/bin/env python3

import ipaddress


class Validators:
    """Class with static validation methods"""

    @staticmethod
    def is_number(value: str) -> bool:
        """Check if provided value is numeric

        :return: True if value is numeric. False otherwise
        :rtype: bool
        """

        try:
            float(value)
            return True
        except ValueError:
            pass

        return False

    @staticmethod
    def is_ip(value: str) -> bool:
        """Check if provided value is numeric

        :return: True if value is numeric. False otherwise
        :rtype: bool
        """

        try:
            ipaddress.ip_address(value)
            return True
        except ValueError:
            pass

        return False
