import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("C://Users//anurag.mishra.FPS//PycharmProjects//SMA_POM_UnitTestFramework")
from pageObjects.LoginPage import LoginPage
from pageObjects.ChoosePurchaseOption import ChoosePurchaseOption
from pageObjects.ChoosePurchaseOption2 import ChoosePurchaseOption2
from pageObjects.PaymentOption import PaymentOption
from pageObjects.EFT_Details import EFT_Details
from pageObjects.CompletionPage import CompletionPage
from testData.TestData import TestData


class GuestFees_EFT(unittest.TestCase):
    # Variables
    # ContractNumber = '4007845566', 4003186560
    # ContractNumber = '4007762907'
    # baseURL = "http://172.24.14.137/VPay/?ContractNumber="+ContractNumber+"&Context=VEnquiry&ClubCostCentreNumber=100"
    # username = "sadieka.price"
    # password = "Virgin123"

    objTD = TestData()
    username = objTD.username
    password = objTD.password
    baseURL = objTD.baseURL
    AmountTendered = objTD.EFTAmountTendered
    BankName = objTD.BankName
    BranchName = objTD.BranchName
    BranchCode = objTD.BranchCode
    AccountNumber = objTD.AccountNumber
    AccountHolder = objTD.AccountHolder

    driver = webdriver.Chrome(executable_path="C:\WebDriver\chromedriver.exe")
    driver.implicitly_wait(10)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_GuestFee_EFT(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        self.driver.save_screenshot(
            "C:/Users/anurag.mishra.FPS/PycharmProjects/SMA_POM_UnitTestFramework/screenshot/1Login.png")
        lp.clickLogin()
        time.sleep(2)
        self.assertEqual("VPAY", self.driver.title, "Login Failed")
        self.driver.save_screenshot(
            "C:/Users/anurag.mishra.FPS/PycharmProjects/SMA_POM_UnitTestFramework/screenshot/2ChoosePurchaseOption1.png")

        objPO = ChoosePurchaseOption(self.driver)
        objPO.clickGuestFees()
        time.sleep(2)
        self.driver.save_screenshot(
            "C:/Users/anurag.mishra.FPS/PycharmProjects/SMA_POM_UnitTestFramework/screenshot/3ChoosePurchaseOption2.png")

        objPO2 = ChoosePurchaseOption2(self.driver)
        objPO2.clickGuestFees()
        time.sleep(1)
        self.driver.save_screenshot(
            "C:/Users/anurag.mishra.FPS/PycharmProjects/SMA_POM_UnitTestFramework/screenshot/4PaymentOption.png")

        objPayment = PaymentOption(self.driver)
        objPayment.clickEFT()
        time.sleep(1)

        objEFTDetails = EFT_Details(self.driver)
        # objEFTDetails.setAmountTendered(self.AmountTendered)
        objEFTDetails.setBankName(self.BankName)
        objEFTDetails.setBranchName(self.BranchName)
        # objEFTDetails.setBranchCode(self.BranchCode)
        objEFTDetails.setAccountNumber(self.AccountNumber)
        objEFTDetails.setAccountHolder(self.AccountHolder)
        self.driver.save_screenshot(
            "C:/Users/anurag.mishra.FPS/PycharmProjects/SMA_POM_UnitTestFramework/screenshot/5EFT_Details.png")
        objEFTDetails.clickSubmit()
        time.sleep(5)
        self.driver.save_screenshot(
            "C:/Users/anurag.mishra.FPS/PycharmProjects/SMA_POM_UnitTestFramework/screenshot/6PaymentConformation.png")
        objEFTDetails.clickPopUpSubmit()
        time.sleep(5)
        self.driver.save_screenshot(
            "C:/Users/anurag.mishra.FPS/PycharmProjects/SMA_POM_UnitTestFramework/screenshot/7CompletionPage.png")
        TestResult = self.driver.find_element_by_xpath("//*[@id='page']/div/div[1]/h1").is_displayed()
        self.assertEqual(TestResult, True, "Transaction Failed")
        print("test case completed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C://Users//anurag.mishra.FPS//PycharmProjects//SMA_POM_UnitTestFramework//reports'))
