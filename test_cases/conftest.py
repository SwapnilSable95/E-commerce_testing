import pytest
from selenium import webdriver
from utilities import readProperties
import os
from datetime import datetime





from utilities.readProperties import ReadConfig
from pageobject.loginpage import Loginpage

@pytest.fixture
def setup():
    url=ReadConfig.getApplicationURL()
    driver=webdriver.Edge(executable_path='C:\Users\swapnil\Downloads\edgedriver_win64 (1)\msedgedriver.exe')
    driver.get(url)

    yield driver
    driver.quit()



# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'E-commerce'
    config._metadata['Tester'] = 'Swapnil'




# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)









