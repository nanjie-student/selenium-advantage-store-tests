from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# === 启动浏览器 ===
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# === 登录 ===
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# === 添加两个商品到购物车 ===
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)

# === 进入购物车页面 ===
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# === 获取购物车中所有商品名称 ===
cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
cart_item_names = [item.text for item in cart_items]
print("🛒 当前购物车商品名称列表：", cart_item_names)

# === 预期添加的商品 ===
expected_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

# === 检查商品是否都在购物车中 ===
missing_items = [item for item in expected_items if item not in cart_item_names]

if not missing_items:
    print("所有商品名称匹配，测试通过")
else:
    print(f"以下商品未出现在购物车中: {missing_items}")

# === 截图购物车页面（可选）===
driver.save_screenshot("sauce_cart_name_check.png")

# === 关闭浏览器 ===
driver.quit()
