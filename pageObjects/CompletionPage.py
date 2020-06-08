from selenium import webdriver


class CompletionPage():
    # Locators of CreditCard elements
    Button_Done_xpath = "//*[@id='page']/div/div[3]/a[3]"
    Button_PrintReceipt_xath = "//*[@id='page']/div/div[3]/a[2]"
    Button_MakeAnotherPAyment_xpath = "//*[@id='page']/div/div[3]/a[1]"
    element_Complete_xpath = "//*[@id='page']/div/div[1]/h1"

    def __init__(self, driver):
        self.driver = driver

    def verifyComplete(self):
        self.driver.find_element_by_xpath(self.element_Complete_xpath)

    def clickDone(self):
        self.driver.find_element_by_xpath(self.Button_Done_xpath).click()

    def clickPrintReceipt(self):
        self.driver.find_element_by_xpath(self.Button_PrintReceipt_xath).click()

    def clickMakeAnotherPAyment(self):
        self.driver.find_element_by_xpath(self.Button_MakeAnotherPAyment_xpath).click()
