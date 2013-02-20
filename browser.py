#!/usr/bin/env python
from selenium import webdriver
import unittest
import time

# Local modules
from init import get_config
from chromedriver_video import Video

# Get configuration options
CFG = get_config()


class AmIndVideoPlay(unittest.TestCase):

    def setUp(self):
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

    def test_video_play_on_am_ind(self):
        driver = self.driver

        # Visit a page
        driver.get(CFG['home_url'])

        # Loop over all three tabs
        for id in range(1, 4):
            self.play_video_tab(id)

        for id in range(1, 4):
            self.play_video_tab(id)

    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
