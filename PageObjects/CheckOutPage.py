from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import Confirmpage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    item_titles = (By.CSS_SELECTOR, ".card-title")
    item_addbuttons = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.PARTIAL_LINK_TEXT, "Checkout")
    checkoutButton_final = (By.XPATH, "//td/button[contains(@class, 'btn-success')]")

    def getItemTitles(self):
        return self.driver.find_elements(*CheckOutPage.item_titles)

    def getItemButtons(self):
        return self.driver.find_elements(*CheckOutPage.item_addbuttons)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutButton)

    def getCheckoutButtonFinal(self):
        self.driver.find_element(*CheckOutPage.checkoutButton_final).click()
        ConfirmPage = Confirmpage(self.driver)
        return ConfirmPage
