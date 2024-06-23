# from selenium.webdriver.common.by import By
#
#
# class Loginpage:
#
#     input_Username_id='loginusername'
#     input_password_id='loginpassword'
#     btn_login_xpath='//*[@id="logInModal"]/div/div/div[3]/button[2]'
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def enter_username(self,username):
#
#         self.driver.find_element(By.ID,self.input_Username_id).send_keys(username)
#
#     def enter_password(self,password):
#         self.driver.find_element(By.ID,self.input_password_id).send_keys(password)
#     def click_on_loginbtn(self):
#         self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
#     def handle_alert(self):
#         alert = self.driver.switch_to.alert
#         alert.accept()


# pageobject/loginpage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Loginpage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "loginpassword"))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_on_loginbtn(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))
        )
        login_button.click()
