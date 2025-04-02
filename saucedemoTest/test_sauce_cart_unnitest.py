import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSauceDemoCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

        # 登录
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def test_add_items_to_cart(self):
        driver = self.driver

        # 添加两个商品
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)

        # 进入购物车页面
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # 获取购物车中所有商品名称
        cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_item_names = [item.text for item in cart_items]
        print("当前购物车商品名称列表：", cart_item_names)

        # 预期商品
        expected_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

        for item in expected_items:
            self.assertIn(item, cart_item_names, f"未找到商品：{item}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
