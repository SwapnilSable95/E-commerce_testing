from selenium.webdriver.common.by import By

class Signup:
    input_Username_id='sign-username'
    input_Password_id='sign-password'
    btn_sign_up_xpath='//*[@id="signInModal"]/div/div/div[3]/button[2]'


    def __init__(self,driver):
         self.driver=driver

    def enter_Username(self,Username):
        self.driver.find_element(By.ID,self.input_Username_id).send_keys(Username)
    def enter_password(self,password):
        self.driver.find_element(By.ID,self.input_Password_id).send_keys(password)
    def click_signup_btn(self):
        self.driver.find_element(By.XPATH,self.btn_sign_up_xpath).click()
    def handle_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()





