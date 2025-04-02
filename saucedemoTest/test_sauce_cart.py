import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSauceCart:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

        # 登录
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    # def test_login_fail(self):
    #     driver = self.driver

    #     # 输入错误密码
    #     driver.find_element(By.ID, "user-name").clear()
    #     driver.find_element(By.ID, "password").clear()
    #     driver.find_element(By.ID, "user-name").send_keys("standard_user")
    #     driver.find_element(By.ID, "password").send_keys("wrong_password")
    #     driver.find_element(By.ID, "login-button").click()
    #     time.sleep(2)

    #     # 获取错误提示信息
    #     error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    #     print("登录失败提示：", error_msg)

    #     # 断言提示内容包含特定关键词
    #     assert "Username and password do not match" in error_msg or "Epic sadface" in error_msg


    def teardown_method(self):
        self.driver.quit()

    def test_add_items_and_verify_names(self):
        driver = self.driver

        # 添加商品
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
            assert item in cart_item_names, f"缺少商品：{item}"
