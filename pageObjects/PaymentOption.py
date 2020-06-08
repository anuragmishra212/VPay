class PaymentOption():
    # Locators of CreditCard elements
    Link_CreditCard_xpath = "//*[@id='2']"
    Link_ReceiptCardSlip_xpath = "//*[@id='3']"
    Link_EFT_xpath = "//*[@id='4']"

    def __init__(self, driver):
        self.driver = driver

    def clickCreditCard(self):
        self.driver.find_element_by_xpath(self.Link_CreditCard_xpath).click()

    def clickReceiptCardSlip(self):
        self.driver.find_element_by_xpath(self.Link_ReceiptCardSlip_xpath).click()

    def clickEFT(self):
        self.driver.find_element_by_xpath(self.Link_EFT_xpath).click()
