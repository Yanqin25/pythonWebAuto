# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import time
import os
option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")
driver = webdriver.Chrome(options=option,executable_path=r"D:\usefulPlugin\chromedriver.exe")
driver.get("http://1807050057.pre-pool1-site.make.yun300.cn/blank23.html")
basePath = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(basePath, 'screenshot/code.png')
time.sleep(1)
driver.save_screenshot(filepath)
try:
    codeImg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='Verification Code']")))
    print(codeImg.get_attribute('alt'))
    left = codeImg.location["x"]
    right = left+codeImg.size["width"]
    top = codeImg.location["y"]
    bottom = codeImg.size["height"]+top
    Image.open(filepath).crop((left, top, right, bottom)).save(filepath)

    img=Image.open(filepath)
    text=pytesseract.image_to_string(img)
    print(text)
finally:
    driver.quit()
