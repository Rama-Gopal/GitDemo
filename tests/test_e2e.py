from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        CheckoutPage = homePage.shopItems()
        log.info("getting all the card titles")
        item_titles = CheckoutPage.getItemTitles()
        c = -1
        for item_title in item_titles:
            c += 1
            if item_title.text == 'Blackberry':
                CheckoutPage.getItemButtons()[c].click()

        CheckoutPage.getCheckoutButton().click()
        ConfirmPage = CheckoutPage.getCheckoutButtonFinal()
        log.info("Entering country name as India")
        ConfirmPage.getCountryField().send_keys("India")
        #  time.sleep(10)
        self.verifyLinkPresence("India")
        ConfirmPage.getCountrySuggestion().click()
        ConfirmPage.getCheckBox().click()
        ConfirmPage.getSubmitButton().click()
        successText = ConfirmPage.getSuccessText().text
        log.info("Text received from Appliction is"+successText)
        assert "Success! Thank you!" in successText
        self.driver.get_screenshot_as_file("screen.png")
