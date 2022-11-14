"""
複数ボタンを列指定で画面を作る
tkinterで作成

taikin.py

2022/11/14
"""
from tkinter import *
from tkinter import ttk
import getpass
import os
import sys
import time



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



	
userName = getpass.getuser()
print(userName)


def shutDown():
	os.system('shutdown -s')


def button_on(text):
    print(text)
    sys.exit()


def no_dakoku_end():
	print('打刻せずPC終了')
	time.sleep(2)
	print('stop2')
	shutDown()

def owari():
	sys.exit()

# root画面を作る
width = 140 
height= 50
btn_n = 0
retu = 4
bottan_total = 6

# 縦の計算はちといい加減
total_width = 10*2 + width*retu + (190-140)*(retu-1)
totla_height = 20 + 80*(bottan_total//retu) + 50 
win_size = str(total_width) + 'x' + str(totla_height)

root = Tk()
root.title('日程選択')
root.geometry(win_size)
#root.resizable(False, False)
#frame1 = ttk.Frame(root, padding=(32))
#frame1.grid()

#rame2 = ttk.Frame(frame1, padding=(0, 5))
#frame2.grid(row=2, column=1, sticky=W)

text_n = ['20221005AM / 30人','20221005PM / 25人','20221223','44444','5555','6666']


btn_n = 0
button0 = ttk.Button(text=text_n[btn_n],command=lambda:(button_on(text_n[0])))
button0.place(x=10+190*(btn_n % retu ), y=20+80*(btn_n // retu), width=width, height=height)

btn_n = btn_n + 1
button1 = ttk.Button(text=text_n[btn_n], command=lambda:(button_on(text_n[1])))
button1.place(x=10+190*(btn_n % retu ), y=20+80*(btn_n // retu), width=width, height=height)

btn_n = btn_n + 1
button2 = ttk.Button(text=text_n[btn_n], command=lambda:(button_on(text_n[2])))
button2.place(x=10+190*(btn_n % retu), y=20+80*(btn_n // retu), width=width, height=height)

btn_n = btn_n + 1
button3 = ttk.Button(text=text_n[btn_n], command=lambda:(button_on(text_n[3])))
button3.place(x=10+190*(btn_n % retu), y=20+80*(btn_n // retu), width=width, height=height)

btn_n = btn_n + 1
button4 = ttk.Button(text=text_n[btn_n], command=lambda:(button_on(text_n[4])))
button4.place(x=10+190*(btn_n % retu), y=20+80*(btn_n // retu), width=width, height=height)

btn_n = btn_n + 1
button5 = ttk.Button(text=text_n[btn_n], command=lambda:(button_on(text_n[5])))
button5.place(x=10+190*(btn_n % retu), y=20+80*(btn_n // retu), width=width, height=height)


root.mainloop()