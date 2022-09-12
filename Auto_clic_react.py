from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
import credentials
import os
import logging

# create logger
logger = logging.getLogger('auto_click_react')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

if __name__ == '__main__':

    # FireFox binary path (Must be absolute path)
    FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')
    # FIREFOX_BINARY = FirefoxBinary('/usr/bin/firefox')
    
    # FireFox Options
    FIREFOX_OPTS = Options()
    FIREFOX_OPTS.headless = True
    FIREFOX_OPTS.binary_location = FIREFOX_BINARY

    geckodriverPath = os.path.join(os.getcwd(), "geckodriver.exe" if  os.name == 'nt' else "/usr/bin/geckodriver")

    logger.info("Starting Firefox")

    driver = webdriver.Firefox(
        service=Service(geckodriverPath),
        options=FIREFOX_OPTS
        )
    driver.get(f"https://www.messenger.com/t/{credentials.FB_GROUPE}")

    logger.info("Sleep 2sec and click on accept cookies")
    time.sleep(2)

    driver.find_element(By.XPATH, '//button[text()="Allow essential and optional cookies"]').click()

    logger.info("Login")
    driver.find_element(By.ID, "email").send_keys(credentials.FB_USERNAME)
    driver.find_element(By.ID, "pass").send_keys(credentials.FB_PASSWORD)
    driver.find_element(By.ID, "loginbutton").click()

    logger.info("Sleep 5sec and start loop")
    time.sleep(5)

    previous = None

    while True:
        try:
            elem = driver.find_elements(By.CLASS_NAME, "hg9jxets")[-1]
            if elem.text != credentials.FB_NAME:
                coucou = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/span[2]/div/span")
                if elem != previous:
                    coucou.click()
                    previous = elem
                    logger.info("Click on react")
                else:
                    logger.info("Already click on react")
                    time.sleep(5)
        except Exception as e:
            logger.error(e)
            pass
