#!/usr/bin/env python

""" Get Kiosk config options """

import ConfigParser
import collections
import os
import sys

SCRIPT_PATH, __ = os.path.split(sys.argv[0])


def get_config():
    """Load kiosk config """
    config = ConfigParser.ConfigParser()
    config_file = SCRIPT_PATH + "/kiosk.cfg"
    config.read(config_file)

    browser = collections.namedtuple('name', 'value')

    browser = {'home_url': config.get("kiosk", "home_url"),
               'kiosk': config.getboolean("kiosk", "kiosk"),
               'user_agent': config.get("kiosk", "user_agent")
               }

    return browser
