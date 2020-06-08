class TestData():
    # LoginCreds
    ContractNumber = '4003186560'
    baseURL = "http://172.24.14.137/VPay/?ContractNumber=" + ContractNumber + "&Context=VEnquiry&ClubCostCentreNumber=100"
    username = "sadieka.price"
    password = "Virgin123"

    # CreditCardVariables
    AmountTendered = "120"
    CreditCardNumber = "4000000000000002"
    CardHolder = "Anurag Mishra"
    ExpiryMonth = "July"
    ExpiryYear = "2022"
    CVVNumber = "555"

    # EFTVariables
    EFTAmountTendered = "120"
    BankName = "ABSA BANK"
    AccountType = ""
    BranchName = "UNIVERSAL BRANCH CODE"
    BranchCode = "632005"
    AccountNumber = "632005002"
    AccountHolder = "Anurag Mishra"
