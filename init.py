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
    config_file = SCRIPT_PATH + "/browser.cfg"
    config.read(config_file)

    browser = collections.namedtuple('name', 'value')

    browser = {'home_url': config.get("browser", "home_url"),
               'kiosk': config.getboolean("browser", "kiosk"),
               'user_agent': config.get("browser", "user_agent")
               }

    return browser
