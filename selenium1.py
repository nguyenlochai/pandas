import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

usernames = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]
password = "secret_sauce"
data = []

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--guest") 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_opt)

for username in usernames:
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # nếu thành công đăng nhập
    if "inventory" in driver.current_url:
        names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        for n, p in zip(names, prices):
            data.append({
                "username": username,
                "product_name": n.text,
                "price": p.text
            })
        try:
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(0.5)
            driver.find_element(By.ID, "logout_sidebar_link").click()
            time.sleep(1)
        except:
            pass
    else:
        data.append({
            "username": username,
            "product_name": "LOGIN FAILED",
            "price": ""
        })

driver.quit()

df = pd.DataFrame(data)
df.to_excel("productsDemo.xlsx", index=False)
print("Đã lưu file productsDemo.xlsx")
