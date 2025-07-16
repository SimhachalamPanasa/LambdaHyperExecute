from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_Lambda():
    driver = webdriver.Chrome()
    driver.get("https://accounts.lambdatest.com/register")
    driver.maximize_window()
    driver.implicitly_wait(5)
    assert "Free Cross Browser Testing Tool on Cloud - LambdaTest" in driver.title
    time.sleep(2)
    driver.quit()



