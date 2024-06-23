
import time
from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from pageobject.store_page import Store
from pageobject.loginpage import Loginpage

class Test_Logout:
    def test_successful_logout(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(ReadConfig.getApplicationURL())

        self.storepageobj = Store(self.driver)
        self.loginpageobj = Loginpage(self.driver)

        # Log in to the application
        self.storepageobj.click_on_login()
        self.loginpageobj.enter_username("Automation12345")
        self.loginpageobj.enter_password("swapnil")
        self.loginpageobj.click_on_loginbtn()
        time.sleep(3)



        # Log out from the application
        self.storepageobj.click_on_logout()
        time.sleep(3)
        self.signuplink=self.driver.find_element(By.ID,'signin2')
        if self.signuplink.is_displayed():
            print ("Logout test pass")
        else:
            print ("Logout test fail")

        # self.driver.close()
