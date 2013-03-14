#!/usr/bin/env python
from selenium import webdriver
import unittest
import time
import re

# Local modules
from init import get_config
from chromedriver_video import Video

# Get configuration options
CFG = get_config()


class AmIndVideoPlay(unittest.TestCase):
    """Test the video playback on the American Indian exhibit kiosks

    Extends the unittest class. Any methods starting with test_ will better
    run as tests.
    """

    def setUp(self):
        """Setup the Chome browser for testing """
        options = webdriver.ChromeOptions()

        # Define a custom User Agent
        user_agent = '--user-agent="' + CFG['user_agent'] + '"'
        options.add_argument(user_agent)

        # Setup the full screen kiosk
        if CFG['kiosk']:
            options.add_argument('--kiosk')

        # Alternatively launch the webdriver Firefox browser
        # test whether Firefox loads the videos better

        # Launch a Chrome instance with the appropriate options
        chrome_paths = ('c:\Program Files\chromedriver.exe',
                        'c:\Program Files (x86)\chromedriver.exe')
        # Try to launch the Chrome driver without any path details
        try:
            self.driver = webdriver.Chrome(chrome_options=options)
        # If it raises an exception try looping through the path options
        except webdriver.chrome.webdriver.WebDriverException:
            for chrome_path in chrome_paths:
                try:
                    self.driver = webdriver.Chrome(chrome_path,
                                                   chrome_options=options)
                except webdriver.chrome.webdriver.WebDriverException:
                    pass
                else:
                    break

    def test_kiosk(self):
        """Launch a chrome kiosk instance """
        driver = self.driver

        # Visit a page
        driver.get(CFG['home_url'])

        self.check_domain(driver)

    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

    def check_domain(self):
        """Check that you are on the specified domain

        If the user navigates away return to the homepage in the CFG.
        """
        driver = self.driver
        while True:
            current_url = driver.current_url
            match = re.search('.*projects.smm.org.*', current_url)
            if match:
                pass
            else:
                driver.get(CFG['home_url'])

    def play_video_tab(self, id):
        driver = self.driver
        id = str(id)

        # Go to the defined tab, expand video, play video
        driver.find_element_by_xpath("//div[@id='tabs']/ul/\
                                     li[@id='" + id + "']/a").click()
        time.sleep(1)  # Give the video time to display
        driver.find_element_by_xpath("//div[@id='jim-" + id + "']\
                                     /div[@class='playBtn']/a").click()
        element = driver.find_element_by_xpath("//div\
                                               [@id='jim-" + id + "']/video")
        video = Video(element)

        # Play the video and wait for it to finish
        print("Playing video {0}".format(id))
        print("Duration: {0}".format(video.duration))
        video.play()
        # At this step we should check every few seconds that the video is
        # playing properly. If so then the video has passed the test.
        time.sleep(video.duration + 1)  # Pad the duration a second


if __name__ == "__main__":
    unittest.main()
