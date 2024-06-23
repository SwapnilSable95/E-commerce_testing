# import time
# from selenium.webdriver.common.by import By
#
# from pageobject.store_page import Store
# from utilities.readProperties import ReadConfig
#
# class Test_Product_Browsing:
#     def test_products_displayed_on_homepage(self, setup):
#         self.driver = setup
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         self.driver.get(ReadConfig.getApplicationURL())
#
#         self.storepageobj = Store(self.driver)
#
#         # Verify products are displayed on the homepage
#         products = self.storepageobj.get_all_products()
#
#         assert len(products) > 0, "No products displayed on the homepage."
#
#         for product in products:
#
#             product_name = product.find_element(By.CLASS_NAME, "card-title").text
#             print (product_name)
#             assert product_name, "Product name is missing."
#
#
#
#
#
#
#
#     def test_product_categories_navigation(self, setup):
#         self.driver = setup
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         self.driver.get(ReadConfig.getApplicationURL())
#
#         self.storepageobj = Store(self.driver)
#
#         # Categories to test
#         # categories = ["Phones", "Laptops", "Monitors"]
#         self.storepageobj.click_on_categori('Monitors')
#         time.sleep(3)
#         products = self.storepageobj.get_all_products()
#         for product in products:
#
#             product_name = product.find_element(By.CLASS_NAME, "card-title").text
#             print (product_name)
#             assert product_name, "Product name is missing."
#
#
#
#
#             self.driver.get(ReadConfig.getApplicationURL())
#             time.sleep(2)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from pageobject.store_page import Store
from utilities.readProperties import ReadConfig

class Test_Product_Browsing:
    def test_products_displayed_on_homepage(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(ReadConfig.getApplicationURL())

        self.storepageobj = Store(self.driver)

        # Verify products are displayed on the homepage
        products = self.storepageobj.get_all_products()

        assert len(products) > 0, "No products displayed on the homepage."

        for product in products:
            self.verify_product_details(product)

    def test_product_categories_navigation(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(ReadConfig.getApplicationURL())

        self.storepageobj = Store(self.driver)

        # Categories to test
        self.storepageobj.click_on_categori('Monitors')
        time.sleep(3)
        products = self.storepageobj.get_all_products()
        assert len(products) > 0, "No products displayed in the 'Monitors' category."

        for product in products:
            self.verify_product_details(product)

        # Navigate back to the home page
        self.driver.get(ReadConfig.getApplicationURL())
        time.sleep(2)

    def verify_product_details(self, product):
        max_retries = 3
        retries = 0

        while retries < max_retries:
            try:
                product_name = product.find_element(By.CLASS_NAME, "card-title").text
                print(product_name)
                assert product_name, "Product name is missing."
                return  # Exit the function if successful
            except StaleElementReferenceException:
                retries += 1
                time.sleep(1)  # Wait a bit before retrying
                if retries == max_retries:
                    raise


