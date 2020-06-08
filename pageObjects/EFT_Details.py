class EFT_Details():
    # Locators of CreditCard elements
    EditBox_AmountTendered_xpath = "//*[@id='onceOffDebitForm']/fieldset/div[2]/div/input"
    DropDown_BankName_xpath = "//*[@id='bankName']"
    DropDown_BranchName_xpath = "//*[@id='brnchId']"
    EditBox_BranchCode_xpath = "//*[@id='onceOffDebitForm']/fieldset/div[5]/div[2]/input"
    EditBox_AccountNumber_xpath = "//*[@id='aNum']"
    EditBox_AccountHolder_xpath = "//*[@id='fDate']/div[2]/input"
    Button_Submit_xptah = "//*[@id='onceOffDebitForm']/div[2]/button"
    Button_Cancel_xptah = "//*[@id='onceOffDebitForm']/div[2]/a"
    Button_PopUpSubmit_xpath = "//*[@id='OkButton']"

    # EFTAmountTendered = "120"
    # BankName = "ABSA BANK"
    # AccountType = ""
    # BranchCode = "632005"
    # AccountNumber = "632005002"
    # AccountHolder = "Anurag Mishra"

    def __init__(self, driver):
        self.driver = driver

    # ele = self.driver.find_element_by_xpath(self.EditBox_BranchCode_xpath

    def setAmountTendered(self, AmountTendered):
        self.driver.find_element_by_xpath(self.EditBox_AmountTendered_xpath).send_keys(AmountTendered)

    def setBankName(self, BankName):
        self.driver.find_element_by_xpath(self.DropDown_BankName_xpath).send_keys(BankName)

    def setBranchName(self, BranchName):
        self.driver.find_element_by_xpath(self.DropDown_BranchName_xpath).send_keys(BranchName)

    def setBranchCode(self, BranchCode):
        self.driver.find_element_by_xpath(self.EditBox_BranchCode_xpath).send_keys(BranchCode)

    def setAccountNumber(self, AccountNumber):
        self.driver.find_element_by_xpath(self.EditBox_AccountNumber_xpath).send_keys(AccountNumber)

    def setAccountHolder(self, AccountHolder):
        self.driver.find_element_by_xpath(self.EditBox_AccountHolder_xpath).send_keys(AccountHolder)

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.Button_Submit_xptah).click()

    def clickCancel(self):
        self.driver.find_element_by_xpath(self.Button_Cancel_xptah).click()

    def clickPopUpSubmit(self):
        self.driver.find_element_by_xpath(self.Button_PopUpSubmit_xpath).click()
