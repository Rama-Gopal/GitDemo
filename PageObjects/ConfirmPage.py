from selenium.webdriver.common.by import By


class Confirmpage:

    def __init__(self, driver):
        self.driver = driver

    country_field = (By.ID, "country")
    country_suggestion = (By.LINK_TEXT, "India")
    check_box = (By.CSS_SELECTOR, "label[for='checkbox2']")
    submit_button = (By.CSS_SELECTOR, "input[type='submit']")
    success_text = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def getCountryField(self):
        return self.driver.find_element(*Confirmpage.country_field)

    def getCountrySuggestion(self):
        return self.driver.find_element(*Confirmpage.country_suggestion)

    def getCheckBox(self):
        return self.driver.find_element(*Confirmpage.check_box)

    def getSubmitButton(self):
        return self.driver.find_element(*Confirmpage.submit_button)

    def getSuccessText(self):
        return self.driver.find_element(*Confirmpage.success_text)
