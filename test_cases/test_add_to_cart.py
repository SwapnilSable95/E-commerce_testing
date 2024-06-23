import time
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from pageobject.store_page import Store
from selenium.webdriver.common.action_chains import ActionChains

class Test_Add_Product_To_Cart:
    def test_add_last_product_to_cart(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(ReadConfig.getApplicationURL())

        self.storepageobj = Store(self.driver)



        # Navigate to the last page
        self.storepageobj.navigate_to_last_page()
        time.sleep(3)
        products=self.storepageobj.get_all_products()
        print (len(products))
        last_product = products[-1]
        print (last_product.text)
        self.action=ActionChains(self.driver)


        last_product_link = last_product.find_element(By.XPATH,"//*[@id='tbodyid']/div[6]/div/div/h4")
        self.action.move_to_element(last_product_link).click().perform()
        time.sleep(3)
        self.storepageobj.click_on_add_to_cart()
        time.sleep(2)
        self.storepageobj.handle_alert()
        self.storepageobj.click_cart_link()
        time.sleep(3)
        self.product_title=self.driver.find_element(By.XPATH,'//*[@id="tbodyid"]/tr/td[2]')

        if self.product_title.is_displayed():
            print ("Add to cart test pass")

        else:
            print ("Add to cart test fail")

        # self.driver.close()

