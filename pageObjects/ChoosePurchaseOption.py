class ChoosePurchaseOption():
    # Locators of all the elements
    Link_Sundry_xpath = "//*[@id='page']/div/div[2]/button[2]"
    Link_GuestFees_xpath = "//*[@id='page']/div/div[2]/button[1]"
    Link_MembershipFees_xpath = "//*[@id='page']/div/div[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def clickGuestFees(self):
        self.driver.find_element_by_xpath(self.Link_GuestFees_xpath).click()

    def clickSundry(self):
        self.driver.find_element_by_xpath(self.Link_Sundry_xpath).click()

    def clickMembershipFees(self):
        self.driver.find_element_by_xpath(self.Link_MembershipFees_xpath).click()
