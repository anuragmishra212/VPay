class ChoosePurchaseOption2():
    # Locators of GuestFee elements
    Link_Back_xpath = "//*[@id='page']/div/div[2]/div[2]/button"
    Link_GuestFee_xpath = "//*[@id='page']/div/div[2]/div[2]/a[1]"
    Link_GuestFeeClubVMax_id = "guestPopUp"
    PopUp_EditBox_id = "guestTextBox"
    PopUp_Button_Submit_id = "guestCombobox"
    PopUp_Button_Close_id = "closeButton"
    NumberOfClubVMaxGuests = '1'
    NumberOfTowels = '1'
    NumberOfHolidayCampDays = '1'

    # Locators of Sundry elements
    Link_ParkingTag_xpath = "//*[@id='page']/div/div[2]/div[3]/a[1]"
    Link_ClubVBirthdayPartyAllocation_xpath = "//*[@id='page']/div/div[2]/div[3]/a[2]"
    Link_StaffUniform_xpath = "//*[@id='page']/div/div[2]/div[3]/a[3]"
    Link_Stationery_xpath = "//*[@id='page']/div/div[2]/div[3]/a[4]"
    Link_TowelService_xpath = "//*[@id='towelPopUp']"
    Link_KidsHolidayCamps_xpath = "//*[@id='HolidayPopUp']"

    def __init__(self, driver):
        self.driver = driver

    # PopUp
    def clickSubmitButton(self):
        self.driver.find_element_by_id(self.PopUp_Button_Submit_id).click()

    def clickCloseButton(self):
        self.driver.find_element_by_id(self.PopUp_Button_Close_id).click()

    def setVmaxGuestEditBox(self):
        self.driver.find_element_by_id(self.PopUp_EditBox_id).send_keys(NumberOfClubVMaxGuests)

    # GuestFees
    def clickBack(self):
        self.driver.find_element_by_xpath(self.Link_Back_xpath).click()

    def clickGuestFees(self):
        self.driver.find_element_by_xpath(self.Link_GuestFee_xpath).click()

    def clickGuestFeeClubVMax(self):
        self.driver.find_element_by_xpath(self.Link_GuestFeeClubVMax_id).click()

    # Sundry
    def clickParkingTag(self):
        self.driver.find_element_by_xpath(self.Link_ParkingTag_xpath).click()

    def clickClubVBirthdayPartyAllocation(self):
        self.driver.find_element_by_xpath(self.Link_ClubVBirthdayPartyAllocation_xpath).click()

    def clickStaffUniform(self):
        self.driver.find_element_by_xpath(self.Link_StaffUniform_xpath).click()

    def clickStationery(self):
        self.driver.find_element_by_xpath(self.Link_Stationery_xpath).click()

    def clickTowelService(self):
        self.driver.find_element_by_xpath(self.Link_TowelService_xpath).click()

    def clickKidsHolidayCamps(self):
        self.driver.find_element_by_xpath(self.Link_KidsHolidayCamps_xpath).click()
