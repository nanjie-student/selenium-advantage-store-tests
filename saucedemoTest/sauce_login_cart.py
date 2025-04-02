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

# === 添加商品到购物车 ===
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

# === 添加第二个商品到购物车 ===
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)

# === 检查购物车图标 ===
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
if cart_icon.text == "2":
    print("商品成功添加到购物车")
else:
    print("添加失败")

# === 可选：点击购物车图标，截图查看购物车内容 ===
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)
driver.save_screenshot("sauce_cart_contents.png")

# === 关闭浏览器 ===
driver.quit()
