# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def debug(format_string, *args, **kwargs):
    logging.debug(format_string, *args, **kwargs)
