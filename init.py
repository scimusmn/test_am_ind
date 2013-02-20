#!/usr/bin/env python

""" Get Kiosk config options """

import ConfigParser
import collections


def get_config():
    """Load kiosk config """
    config = ConfigParser.ConfigParser()
    config.read("browser.cfg")

    browser = collections.namedtuple('name', 'value')

    browser = {'home_url': config.get("browser", "home_url"),
               'kiosk': config.getboolean("browser", "kiosk"),
               'user_agent': config.get("browser", "user_agent")
               }

    return browser
