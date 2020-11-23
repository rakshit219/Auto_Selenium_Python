class LoginPage:
    
    txt_username_id="Email"
    txt_password_id="Password"
    btn_login_xpath="//input[@value='Log in']"
    
    def __init__(self,driver):
        self.driver=driver
        
    def setuseremail(self,username):
        self.driver.find_element_by_id(self.txt_username_id).clear()
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.txt_password_id).clear()
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)
        
    def login(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()