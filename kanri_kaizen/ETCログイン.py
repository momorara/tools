"""
2022/11/12  ETC利用紹介サービス
"""

import time
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

ETC_URL = "https://www2.etc-meisai.jp/etc/R?funccode=1013000000&nextfunc=1013000000"


ID = '005067104'
passWord   = '123456'

driver = Chrome()
driver.get(ETC_URL)

# ログイン処理
login_input = driver.find_element(By.NAME, "risLoginId")
login_input.send_keys(ID)
# driver.find_element(By.ID, "continue").click()

# パスワード入力
password_input = driver.find_element(By.NAME, "risPassword")
password_input.send_keys(passWord)
# サインインボタンをクリック
driver.find_element(By.NAME, "focusTarget").send_keys(webdriver.Keys.ENTER)
time.sleep(10)

