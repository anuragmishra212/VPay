class LoginPage():
    # Locators of all the elements
    editbox_username_name = "username"
    editbox_password_name = "password"
    button_Login_xpath = "//*[@id='page']/div/div[2]/form/input[2]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_name(self.editbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.editbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_Login_xpath).click()
