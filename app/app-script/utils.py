# -*- coding: utf-8 -*-
import sys
import logging
from logging import StreamHandler


def get_logger(mode_name):
    log = logging.getLogger(mode_name)
    log.setLevel(logging.DEBUG)
    handler = StreamHandler(stream=sys.stdout)
    fmt = logging.Formatter(fmt='%(asctime)s: %(message)s')
    handler.setFormatter(fmt)
    log.addHandler(handler)
    return log


log = get_logger(__name__)