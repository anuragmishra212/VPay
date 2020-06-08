class CreditCardDetails():
    # Locators of CreditCard elements
    EditBox_AmountTendered_xpath = "//*[@id='formContent']/fieldset/div[1]/div/input"
    EditBox_CardNumber_xpath = "//*[@id='formContent']/fieldset/div[2]/input"
    EditBox_CardHolder_xpath = "//*[@id='formContent']/fieldset/div[3]/input"
    DropDown_ExpieryMonth_xpath = "//*[@id='ExpiryMonth']"
    DropDown_ExpieryYear_xpath = "//*[@id='ExpiryYear']"
    EditBox_CVV_xpath = "//*[@id='formContent']/fieldset/div[5]/input"
    Button_Cancel_xpth = "//*[@id='formContent']/div[2]/a"
    Button_Submit_xpth = "//*[@id='btnSubmits']"
    Button_PopUpSubmit_xpth = "//*[@id='OkButton']"

    AmountTendered = "120"
    CreditCardNumber = "4000000000000002"
    CardHolder = "Anurag Mishra"
    ExpiryMonth = "July"
    ExpiryYear = "2022"
    CVVNumber = "555"

    def __init__(self, driver):
        self.driver = driver

    def setAmountTendered(self):
        self.driver.find_element_by_xpath(self.EditBox_AmountTendered_xpath).send_keys(self.AmountTendered)

    def setCardNumber(self):
        self.driver.find_element_by_xpath(self.EditBox_CardNumber_xpath).send_keys(self.CreditCardNumber)

    def setCardHolder(self):
        self.driver.find_element_by_xpath(self.Link_ReceiptCardSlip_xpath).send_keys(self.CardHolder)

    def setExpieryMonth(self):
        self.driver.find_element_by_xpath(self.Link_ReceiptCardSlip_xpath).send_keys(self.ExpiryMonth)

    def setExpieryYear(self):
        self.driver.find_element_by_xpath(self.Link_ReceiptCardSlip_xpath).send_keys(self.ExpiryYear)

    def setCVV(self):
        self.driver.find_element_by_xpath(self.Link_ReceiptCardSlip_xpath).send_keys(self.CVVNumber)

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.Button_Submit_xpth).click()

    def clickButton_PopUpSubmit_xpth(self):
        self.driver.find_element_by_xpath(self.Button_PopUpSubmit_xpth).click()
