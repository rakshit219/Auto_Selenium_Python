from PageObjects.LoginPage import LoginPage
from Utilities.LogUtility import Loggen
from Utilities.readProperty import ReadConfig
import pytest

class Test_Login:
    
    logger=Loggen.loggen()
    
    @pytest.mark.sanity
    def test_login(self,setUp):
        self.logger.info("Starting Test_Login testcase")
        self.driver=setUp
        self.logger.info("Login page displayed")
        self.lp=LoginPage(self.driver)
        self.lp.setuseremail(ReadConfig.getUsername())
        self.lp.setpassword(ReadConfig.getPassword())
        self.lp.login()
        exp_title="Dashboard / nopCommerce administration"
        act_title=self.driver.title
        if act_title==exp_title:
            self.logger.info("Login successful")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.error("Login not successful")
            self.driver.close()
            assert False
        
