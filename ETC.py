"""
2022/11/12  ETC利用紹介サービス
2022/12/02	ログインの先に進めた
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from subprocess import CREATE_NO_WINDOW


import time
import os


# ETCページのログイン情報
ID = '383210'
passWord   = ''

# ETCページのURL
ETC_URL = "https://www2.etc-meisai.jp/etc/R?funccode=1013000000&nextfunc=1013000000"


path = os.getcwd() + '/' # 現在のパスを取得
print(path)

# webDriverのパス設定
EdgeDrivwePath = path + "\\msedgedriver.exe"
driver = webdriver.Edge(executable_path=EdgeDrivwePath) 

# ETCページを開く
driver.creationflags = CREATE_NO_WINDOW
driver.get(ETC_URL)

# ログイン処理
element = driver.find_element(by=By.NAME , value="risLoginId")
element.send_keys(ID)

# パスワード入力
element = driver.find_element(by=By.NAME , value="risPassword")
element.send_keys(passWord)

# ログインボタンをクリック
driver.find_element(By.NAME, "focusTarget").send_keys(webdriver.Keys.ENTER)
#time.sleep(10)

# javascriptを実行すれば、「検索条件の指定」画面へ遷移できた。
driver.execute_script("submitPage('frm','/etc/R?funccode=1014000000&nextfunc=1014000000')");


# 年　月　日の範囲指定
element = driver.find_element(by=By.NAME , value="fromYYYY")
select = Select(element)
# セレクト番号は0から始まる。ので注意！！
select.select_by_index(1)

element = driver.find_element(by=By.NAME , value="fromMM")
select = Select(element)
select.select_by_index(10)

element = driver.find_element(by=By.NAME , value="fromDD")
select = Select(element)
select.select_by_index(0)

element = driver.find_element(by=By.NAME , value="toYYYY")
select = Select(element)
select.select_by_index(1)

element = driver.find_element(by=By.NAME , value="toMM")
select = Select(element)
select.select_by_index(10)

element = driver.find_element(by=By.NAME , value="toDD")
select = Select(element)
select.select_by_index(29)

time.sleep(1)
# 検索ボタンを押す
driver.find_element(By.NAME, "focusTarget").send_keys(webdriver.Keys.ENTER)

time.sleep(2)
print('********')

# ボタンが見えるようにスクロール
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# 利用明細ＣＳＶ出力　が押せないのね

driver.forward()
print(driver.current_url)

element = driver.find_element(By.Xpath,"//input[@value='ＣＳＶ']")
element.click()

time.sleep(20)

exit(0)


driver.find_element(By.class_name, value="btn2").send_keys(webdriver.Keys.ENTER)



element = driver.find_element(by=By.NAME , value="利用明細ＣＳＶ出力")
element.click()


#driver.get("https://www2.etc-meisai.jp/etc/R?funccode=1013000000&nextfunc=1013500000")

time.sleep(10)



#driver.find_element(By.NAME, "利用明細ＣＳＶ出力").send_keys(webdriver.Keys.ENTER)

#driver.execute_script("frm","/etc/R?funccode=1013000000&nextfunc=1013500000");



time.sleep(20)
 
# 画面を消さずにプログラム終了
os.kill(driver.service.process.pid,signal.SIGTERM)

