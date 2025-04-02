from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置部分
USERNAME = "guestTest"  
PASSWORD = "guestTest123"  

# 初始化 WebDriver
driver = webdriver.Chrome()
driver.get("https://advantageonlineshopping.com/")
driver.maximize_window()

try:
    # 等待并点击右上角的用户图标，打开登录窗口
    user_icon = driver.find_element(By.ID, "menuUser")
    user_icon.click()

    # 等待登录窗口出现
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    # 输入用户名和密码
    # 输入用户名和密码
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)

    # 等待登录按钮可点击
    # sign_in_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "sign_in_btnundefined"))
    # )
    # sign_in_button.click()

    # 方法二：使用 JavaScript 点击登录按钮
    sign_in_button = driver.find_element(By.ID, "sign_in_btnundefined")
    driver.execute_script("arguments[0].click();", sign_in_button)

    # 验证是否成功登录
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='hi-user containMiniTitle ng-binding']"))
    )
    print("登录成功！")



except Exception as e:
    print(f"登录过程中出现错误: {e}")

finally:
    # 关闭浏览器
    time.sleep(5)  # 保持浏览器打开5秒，便于观察结果
    driver.quit()



