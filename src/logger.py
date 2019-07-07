#!/usr/bin/env python3

import time


class Logger(object):

    LOG_DIR = 'log'
    SCREENSHOT_DIR = 'log/screenshots'

    def log_msg(self, msg):
        tstr = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
        print("%s - %s" % (tstr, msg))
