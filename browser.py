#!/usr/bin/env python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=""')
options.add_argument('--kiosk')

# Launch a Chrome instance with the appropriate options
driver = webdriver.Chrome(chrome_options=options)

# Visit a page
driver.get("http://www.example.com")

driver.quit()
