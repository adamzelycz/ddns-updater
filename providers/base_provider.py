#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from src.logger import Logger


class BaseProvider(object):

    __metaclass__ = ABCMeta

    def __init__(self, logger: Logger, debug: int):
        self.logger = logger
        self.debug = debug

    @abstractmethod
    def get_ip(self, argv=None) -> str:
        raise NotImplementedError
