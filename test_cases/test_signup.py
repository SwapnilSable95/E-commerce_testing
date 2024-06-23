import time

from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from pageobject.store_page import Store
from pageobject.signuppage import Signup
from utilities import randomstring

class Test_signup:


    def test_signup(self,setup):

        self.driver=setup
        self.driver.implicitly_wait(10)
        # self.driver.get(self.url)
        self.driver.maximize_window()
        self.storepageobj=Store(self.driver)
        self.signpageobj=Signup(self.driver)
        self.storepageobj.click_on_sign_up()
        self.username=randomstring.random_string_generator()+'@gmail.com'
        self.signpageobj.enter_Username(self.username)

        self.signpageobj.enter_password('Vinay14trr')
        self.signpageobj.click_signup_btn()
        time.sleep(3)
        self.signpageobj.handle_alert()
        self.act_title=self.driver.title
        self.exp_title="STORE"
        if self.act_title==self.exp_title:
            print("Signup Test Passed")
        else:
             print("Signup Test Failed")

        time.sleep(3)
        # self.driver.close()

    def test_signup_empty_username(self,setup):

        self.driver=setup
        self.driver.implicitly_wait(10)
        # self.driver.get(self.url)
        self.driver.maximize_window()
        self.storepageobj=Store(self.driver)
        self.signpageobj=Signup(self.driver)
        self.storepageobj.click_on_sign_up()

        self.signpageobj.enter_Username('')

        self.signpageobj.enter_password('Vinay14trr')
        self.signpageobj.click_signup_btn()
        time.sleep(3)
        self.signpageobj.handle_alert()
        self.signupbtn=self.driver.find_element(By.XPATH,'//*[@id="signInModal"]/div/div/div[3]/button[2]')

        if self.signupbtn.is_displayed():
            print("Signup Test Pass")
        else:
             print("Signup Test fail")

        time.sleep(3)
        # self.driver.close()






















