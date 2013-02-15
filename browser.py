#!/usr/bin/env python
from selenium import webdriver

# Local modules
from init import get_config

CFG = get_config()
options = webdriver.ChromeOptions()

# Define a custom User Agent
user_agent = '--user-agent="' + CFG['user_agent'] + '"'
options.add_argument(user_agent)

# Setup the full screen kiosk
if CFG['kiosk']:
    options.add_argument('--kiosk')

# Launch a Chrome instance with the appropriate options
driver = webdriver.Chrome(chrome_options=options)

# Visit a page
driver.get(CFG['home_url'])

#driver.quit()
