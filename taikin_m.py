"""
退勤時確認画面
tkinterで作成

taikin.py

2022/10/28
2022/10/31
2022/11/18	パスワード強化
"""
from tkinter import *
from tkinter import ttk

import getpass
import os
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


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
	
	
userName = getpass.getuser()
print(userName)

EdgeDrivwePath = path + "\\msedgedriver.exe"
LysitheaURL = "http://lys.extra.root.kanden.ne.jp/Lysithea/JSP_Files/timeclock/WC160.jsp"

userID = '005' + userName
passWord   = passGet()

def shutDown():
	os.system('shutdown -s')


def dakoku_end():
	print('打刻してPC終了')
	
	# 対応するwebdriverをダウンロードして使う場合
	# driver = webdriver.Edge(executable_path=EdgeDrivwePath) 

	# Webdriver Manager for Python を使う場合
	driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
	
	
	driver.get(LysitheaURL)
	time.sleep(0.5)
	element = driver.find_element(by=By.CLASS_NAME , value="InputTxtL")
	element.send_keys(userID)
	element = driver.find_element(by=By.NAME , value="password")
	element.send_keys(passWord)
	time.sleep(0.5)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='../gif/taikin.png'][type='image']"))).click()
	time.sleep(0.5)
	print('stop1')
	shutDown()


def no_dakoku_end():
	print('打刻せずPC終了')
	time.sleep(2)
	print('stop2')
	shutDown()

def owari():
	sys.exit()

# root画面を作る
root = Tk()
root.title('退勤処理選択')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=2, column=1, sticky=W)


# 打刻してPC終了ボタンを作る
button1 = ttk.Button(
    frame2, text='打刻してPC終了', 
    command=lambda:( 
        dakoku_end(),
        )
    )
button1.pack(side=LEFT)


# 打刻せずPC終了ボタンを作る
button2 = ttk.Button(
    frame2, text='打刻せずPC終了', 
    command=lambda:( 
    	no_dakoku_end(),
    	)
    )
button2.pack(side=LEFT)


# キャンセルボタンを作る
button3 = ttk.Button(
    frame2, text='キャンセル', command=lambda:(owari()))
button3.pack(side=LEFT)

root.mainloop()
