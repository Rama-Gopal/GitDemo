from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, 'email')
    check_box = (By.ID, 'exampleCheck1')
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@type='submit']")
    success_text = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()  #  This step is same as - self.driver.find_element_by_css_selector("a[href*='shop']")
        CheckoutPage = CheckOutPage(self.driver)
        return CheckoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.check_box)

    def getDropDown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit_button)

    def getSuccessText(self):
        return self.driver.find_element(*HomePage.success_text)
