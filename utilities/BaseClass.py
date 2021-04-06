import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        #  logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        fileFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(fileFormat)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionsByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
