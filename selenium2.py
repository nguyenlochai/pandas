import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

base_url = "https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep"
driver.get(base_url)
time.sleep(2)

# Lấy số trang (tìm số lớn nhất trên thanh phân trang)
pages = driver.find_elements(By.CSS_SELECTOR, ".pagination .page-link")
total_pages = 1
for page in pages:
    text = page.text.strip()
    if text.isdigit():
        total_pages = max(total_pages, int(text))

print(f"Đang crawl {total_pages} trang...")

sheet_data = {}

for page in range(1, total_pages + 1):
    print(f"Đang xử lý trang {page}/{total_pages}...")
    driver.get(f"{base_url}?page={page}")
    time.sleep(2)
    elements = driver.find_elements(By.CLASS_NAME, "item_mst") + driver.find_elements(By.CLASS_NAME, "item_mst_o")
    data = []
    for el in elements:
        lines = el.text.strip().split("\n")
        if len(lines) >= 3:
            data.append({
                "Mã số thuế": lines[0].strip(),
                "Tên doanh nghiệp": lines[1].strip(),
                "Ngày cấp": lines[2].strip()
            })
    sheet_data[f"Trang_{page}"] = pd.DataFrame(data)

driver.quit()

with pd.ExcelWriter("doanh_nghiep_mst.xlsx") as writer:
    for sheet_name, df in sheet_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Đã lưu file doanh_nghiep_mst.xlsx")
