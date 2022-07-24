# # automating flipkart and scrapping the pages with the help of intelligent searching
from numpy import product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
# from openpyxl import Workbook

# wb = Workbook()
# ws = wb.active
# l = 2
# ws.cell(row=1, column=1).value = "Product Name"
# ws.cell(row=1, column=2).value = "Price"
# ws.cell(row=1, column=3).value = "Rating"
# ws.cell(row=1, column=4).value = "Image Link"
# ws.cell(row=1, column=5).value = "Product Link"

op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")
driver=webdriver.Chrome(service=Service("D:\chromedriver.exe"),options=op)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

driver.implicitly_wait(3)
try:
    skip_button=driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").send_keys(Keys.ENTER)
except:
    print("Skipping...")

search_box=driver.find_element(by=By.CLASS_NAME,value="_3704LK")

driver.implicitly_wait(3)
product='Mens Wear'
search_box.send_keys(product+ Keys.ENTER)

get_url = driver.current_url #url of the keyword searched for
print(get_url)

time.sleep(10)
driver.save_screenshot(f'{product}.png')

javaScript = "window.scrollBy(0,1080);"
driver.execute_script(javaScript)

driver.save_screenshot(f'{product}1.png')

driver.quit()

