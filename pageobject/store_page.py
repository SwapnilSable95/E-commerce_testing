from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

class Store:
    lnk_signup_id='signin2'
    lnk_login_id='login2'
    cards_xpath='//*[@id="tbodyid"]/div'
    phone_categori_xpath='//div[@id="contcont"]//a[2]'
    laptops_categori_xpath='//div[@id="contcont"]//a[3]'
    moniters_categori_xpath='//div[@id="contcont"]//a[4]'
    cart_title_class='card-title'
    btn_next_xpath = "//*[@id='next2']"
    add_to_cart_btn_xpath = "//*[@id='tbodyid']/div[2]/div/a"
    link_cart_xpath='//*[@id="cartur"]'
    link_logout_id='logout2'


    def __init__(self,driver):
        self.driver=driver

    def click_on_sign_up(self):
        self.action=ActionChains(self.driver)
        self.sign_up_ele=self.driver.find_element(By.ID,self.lnk_signup_id)
        self.action.move_to_element(self.sign_up_ele).click().perform()

    def click_on_login(self):
        self.action=ActionChains(self.driver)
        self.login_ele=self.driver.find_element(By.ID,self.lnk_login_id)
        self.action.move_to_element(self.login_ele).click().perform()
    def get_all_products(self):
        products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.cards_xpath))
        )
        return products

    def click_on_categori(self,r):
        self.driver.find_element(By.LINK_TEXT,r).click()
    def navigate_to_last_page(self):
        while True:
            try:
                next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_next_xpath)))
                next_button.click()
                time.sleep(2)  # Allow time for the next page to load
            except TimeoutException:
                break  # No more next button, we are on the last page

    def click_on_add_to_cart(self):
        self.driver.find_element(By.XPATH,self.add_to_cart_btn_xpath).click()
    def handle_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
    def click_cart_link(self):
        self.action=ActionChains(self.driver)
        self.cart_ele=self.driver.find_element(By.XPATH,self.link_cart_xpath)
        self.action.move_to_element(self.cart_ele).click().perform()

    def click_on_logout(self):
        self.action=ActionChains(self.driver)
        self.logout_ele=self.driver.find_element(By.ID,self.link_logout_id)
        self.action.move_to_element(self.logout_ele).click().perform()
