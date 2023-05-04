from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = input("Enter The Url : ")
driver = webdriver.Chrome()
print("""
------------------------------------

** املأ أوقات الانتظار بالاستغفار  **
اســتغفر الله الــعلي العـــظـــم -
أســتغــفر الله وأتـــوب اليــــه -
- Twitter & Github : @i3koc

-----------------------------------
""")
driver.get(url)
time.sleep(10)
for element in driver.find_elements(By.CLASS_NAME, "vjs-tech"):
    print(element.get_attribute("src"))

driver.close()