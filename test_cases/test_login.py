

from pageobject.store_page import Store
from pageobject.loginpage import Loginpage
import os
import time
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities import xlutils

class Test_Login:
    path = os.path.abspath(os.curdir) + "\\testdata\\LoginData.xlsx"

    def test_login(self, setup):
        self.rows = xlutils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.storepageobj = Store(self.driver)
        self.loginpageobj = Loginpage(self.driver)

        for r in range(2, self.rows + 1):
            self.driver.get(ReadConfig.getApplicationURL())  # Navigate to the home page for each iteration
            self.storepageobj.click_on_login()
            self.username = xlutils.readData(self.path, "Sheet1", r, 1)
            self.password = xlutils.readData(self.path, "Sheet1", r, 2)
            self.exp_result = xlutils.readData(self.path, "Sheet1", r, 3)


            try:
                self.loginpageobj.enter_username(self.username)
                self.loginpageobj.enter_password(self.password)
                self.loginpageobj.click_on_loginbtn()

                # Handle alert if present
                try:
                    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert_text = alert.text
                    alert.accept()

                except (NoAlertPresentException, TimeoutException):
                    actual_result = "No Alert"

                # Compare the actual result with the expected result

            except (ElementNotInteractableException, TimeoutException) as e:
                print (e)
            self.act_title=self.driver.title
            self.exp_title="STORE"
            if self.exp_result=='Valid':
                if self.act_title== self.exp_title:
                    lst_status.append('Pass')
                else:
                    lst_status.append('Fail')
            elif self.exp_result=='Invalid':
                if self.act_title!=self.exp_title:
                    lst_status.append('Fail')
                else:
                    lst_status.append('Pass')
        # self.driver.close()
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
















