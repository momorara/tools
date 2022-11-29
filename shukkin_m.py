"""

login02.py

2022/10/28  リシテア自動打刻を開発スタート
2022/10/31
2022/11/01	打刻成功
2022/11/18	パスワード強化
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.by import By
import signal

import time
import os
import getpass
import sys

from tkinter import *
from tkinter import ttk


userName = getpass.getuser()
print(userName)


path = os.getcwd() + '/' # 現在のパスを取得
print(path)

if not os.path.exists(path + 'pass.txt'):
	# root画面を作る
	root = Tk()
	root.title('---')
	root.resizable(False, False)
	frame1 = ttk.Frame(root, padding=(52))
	frame1.grid()
	# キャンセルボタンを作る
	button1 = ttk.Button(frame1, text='パスワードファイルがありません', command=lambda:(sys.exit()))
	button1.pack(side=LEFT)
	root.mainloop()
	
def passRead():
    with open(path + 'pass.txt') as f:
        passWord = f.read()
    return passWord

# passWordを復号化
def passReturn(passWord):
    index = 1
    passWord = passWord[36:]
    #print(passWord)
    while len(passWord) >30:
        passWord = passWord.replace(passWord[index:36+index],'')
        index = index +1
    return passWord

def passGet():
	text = passRead()
	result = passReturn(text)
	return result


EdgeDrivwePath = path + "\\msedgedriver.exe"
LysitheaURL = "http://lys.extra.root.kanden.ne.jp/Lysithea/JSP_Files/timeclock/WC160.jsp"

userID = '005' + userName
passWord   = passGet()


# 対応するwebdriverをダウンロードして使う場合
driver = webdriver.Edge(executable_path=EdgeDrivwePath) 

# Webdriver Manager for Python を使う場合
#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.creationflags = CREATE_NO_WINDOW
driver.get(LysitheaURL)
time.sleep(0.5)


element = driver.find_element(by=By.CLASS_NAME , value="InputTxtL")
element.send_keys(userID)

element = driver.find_element(by=By.NAME , value="password")
element.send_keys(passWord)

os.system('cls')

time.sleep(0.5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='../gif/shukkin.png'][type='image']"))).click()
os.kill(driver.service.process.pid,signal.SIGTERM)

os.system('cls')

