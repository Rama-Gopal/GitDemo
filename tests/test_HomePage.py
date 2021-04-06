import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheckbox().click()
        # select class provides the methods for handling the options in dropdown
        #  dropdown = Select(homePage.getDropDown())
        #  dropdown.select_by_visible_text('Female')
        #  dropdown.select_by_index(0)
        self.selectOptionsByText(homePage.getDropDown(), getData["gender"])
        homePage.getSubmitButton().click()
        message = homePage.getSuccessText().text

        assert 'success' in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
