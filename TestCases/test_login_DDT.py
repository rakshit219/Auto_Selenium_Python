from PageObjects.LoginPage import LoginPage
from Utilities.LogUtility import Loggen
from Utilities import ExcelUtility
import pytest

class Test_login_DDT:
    
    path=".\\TestData\\testdata.xlsx"
    sheetname="Login data"
    logger=Loggen.loggen()
    
    @pytest.mark.regression
    def test_login_ddt(self,setUp):
        self.logger.info("Starting test_login_ddt testcase")
        self.driver=setUp
        self.logger.info("Login page displayed")
        self.lp=LoginPage(self.driver)
        rows=ExcelUtility.getRowCount(self.path, self.sheetname)
        list_ddt=[]
        
        for i in range(2,rows+1):
            self.email=ExcelUtility.readData(self.path, self.sheetname, i, 1)
            self.pwd=ExcelUtility.readData(self.path, self.sheetname, i, 2)
            self.exp_rst=ExcelUtility.readData(self.path, self.sheetname, i, 3)
            self.lp.setuseremail(self.email)
            self.lp.setpassword(self.pwd)
            self.lp.login()
            
            exp_title="Dashboard / nopCommerce administration"
            act_title=self.driver.title
            
            if act_title==exp_title:
                if self.exp_rst=="Pass":
                    self.logger.info("Test case passed for successsful login")
                    list_ddt.append("Pass")
                    ExcelUtility.writeData(self.path, self.sheetname, i, 4, "Pass")
                elif self.exp_rst=="Fail":
                    self.logger.error("Test case failed for successsful login")
                    list_ddt.append("Fail")
                    ExcelUtility.writeData(self.path, self.sheetname, i, 4, "Fail")
            elif act_title!=exp_title:
                if self.exp_rst=="Fail":
                    self.logger.info("Test case passed for unsuccesssful login")
                    list_ddt.append("Pass")
                    ExcelUtility.writeData(self.path, self.sheetname, i, 4, "Pass")
                elif self.exp_rst=="Pass":
                    self.logger.error("Test case failed for unsuccesssful login")
                    list_ddt.append("Fail")
                    ExcelUtility.writeData(self.path, self.sheetname, i, 4, "Fail")
                    
        if "Fail" in list_ddt:
            self.logger.error("Test_login_DDT failed")
            self.driver.close()
            assert False
        else:
            self.logger.info("Test_login_DDT passed")
            self.driver.close()
            assert True
                    
            