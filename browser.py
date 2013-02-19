#!/usr/bin/env python
from selenium import webdriver
import time

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

driver.find_element_by_xpath("/html[@class='js']/body/div[@id='page-wrapper']\
                             /div[@class='container span-19 last']\
                             /div[@id='page-content']\
                             /div[@class='span-19 last']/div[@id='kiosk-jim']\
                             /div[@class='content clearfix']/div[@id='tabs']\
                             /div[@id='tabs-1']/div[@id='jim-1']\
                             /div[@class='playBtn']/a").click()

time.sleep(3)
driver.quit()
