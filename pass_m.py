"""
パスワード入力画面
tkinterで作成
pass.py 


2022/10/28
2022/10/31
2022/11/11	ドライバーマネージャー対応、インストール機能
2022/11/14	ショートカットコピー
2022/11/18	パスワード強化
"""
from tkinter import *
from tkinter import ttk
import os
import random
import sys
import shutil
import getpass
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from subprocess import CREATE_NO_WINDOW

path = os.getcwd() + '/' # 現在のパスを取得
path1 = os.getcwd()  # 現在のパスを取得
print('path',path)
userID = getpass.getuser()
print('userID:', userID)
LysitheaURL = "http://lys.extra.root.kanden.ne.jp/lysitheabase/jsps/authentication/Logon.jsp"



# 取得したパスワードをファイル保存
def passWrite(passWord):
    # print('1',passWord)
    password111 = passHenge(passWord)
    with open(path + 'pass.txt', mode='w') as f:
        f.write(password111)
        
def passget():
	passText = passRead()
	return passReturn(passText)
	
# passWordを暗号化
def passHenge(passW):
    pass_list = list(passW)
    passWord = ''
    setText = list('abcdefghijklmnopqrstuvwxyz0123456789')
    for pass_text in pass_list:
        random.shuffle(setText) 
        randText = "".join(setText)
        passWord = passWord + randText + pass_text
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

# 保存したパスワードを読込
def passRead():
    with open(path + 'pass.txt') as f:
        passWord = f.read()
    return passWord
	
	
	
	

# 出勤打刻をスタートアップにコピー
# 実体をコピーするとディレクトリが違うのでちゃんと動作しない。
# ショートカットをコピーしようとするとコピーできない
# なのであきらめた。
def startCopy():
	return
	#path_startup = r'C:\Users\\' + userID + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
	#shutil.copyfile(path1 + "\出勤打刻.exe", path_startup + "\出勤打刻.exe")

# 通常場所に使えるドライバーがあるかチェック
def driverCheck():
	try:
		EdgeDrivwePath = path1 + r"\msedgedriver.exe"
		driver = webdriver.Edge(executable_path=EdgeDrivwePath) 
	except:
		return 'err'
		
	# 通常場所のドライバーでリシテアログイン
	driver.creationflags = CREATE_NO_WINDOW
	driver.get(LysitheaURL)
	time.sleep(0.5)
	element = driver.find_element(by=By.CLASS_NAME , value="InputTxtL")
	element.send_keys('005' + userID)
	element = driver.find_element(by=By.NAME , value="password")
	element.send_keys(passget())
	time.sleep(1)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[src='../img/logon.jpg'][type='image']"))).click()
	# 無事リシテアログイン出来たらＯＫ
	os.system('cls')
	time.sleep(3)
	return 'ok'
		
# Webdriver Manager for Python を使って、ドライバーをダウンロード
def driverManeger():
	# 今あるドライバーを削除
	try:os.remove(path+ 'msedgedriver.exe')
	except:pass	
	print('ドライバーエラー使えなかった1')
	# マネージャーのドライバー保存場所のディレクトリを中身ごと削除: 
	try:
		path_driver = r'C:\Users\\' + userID + r'\.wdm\drivers\edgedriver\win64'
		shutil.rmtree(path_driver)
	except:pass
	# ドライバーダウンロードしてログイン
	driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
	# ドライバーコピー
	path_driver = r'C:\Users\\' + userID + r'\.wdm\drivers\edgedriver\win64'
	path_driver = path_driver  + "\\" +  os.listdir(path_driver)[0]+ "\\"
	shutil.copyfile(path_driver + 'msedgedriver.exe', path + 'msedgedriver.exe')
	# ダウンロードしたドライバーでログイン
	driverCheck() # ここで使えるかな？だめなら考える
	print('ドライバーエラー使えなかった2')

def inst_start():
	startCopy()
	if driverCheck() == 'err':
		driverManeger()
	return
	
# root画面を作る
root = Tk()
root.title('パスワード登録')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

# パスワード表示
label2 = ttk.Label(frame1, text='リシテアPassword入力後、試しにリシテアを起動します。', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

# パスワード入力フレームを作る
password = StringVar()
password_entry = ttk.Entry(
    frame1,
    textvariable=password,
    width=20)
password_entry.grid(row=1, column=1)

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=2, column=1, sticky=W)

# 登録ボタンを作る 押された時の動作を指定
button1 = ttk.Button(
    frame2, text='登録',
    command=lambda:( 
        print("%s" % (password.get())),
        passWrite(str(password.get())),
        inst_start(),
        sys.exit()
        )
    )
button1.pack(side=LEFT)

# キャンセルボタンを作る
button2 = ttk.Button(frame2, text='キャンセル', command=lambda:(sys.exit()))
button2.pack(side=LEFT)

root.mainloop()

