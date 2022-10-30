"""
パスワード入力画面
tkinterで作成

2022/10/30

"""
from tkinter import *
from tkinter import ttk
import os
import random

path = os.getcwd() + '/' # 現在のパスを取得
print(path)

# def passRead():
#     with open(path + 'pass.txt') as f:
#         passWord = f.read()
#     return passWord

def passHenge(passWord):
    # print('2',passWord)
    # passWordを軽く暗号化
    setText = list('abcdefghijklmnopqrstuvwxyz0123456789')
    random.shuffle(setText)  
    randText = "".join(setText)
    pass_n = len(passWord) + 11
    if pass_n > 9:
        pass_n = str(pass_n)
    else:
        pass_n = '0' + str(pass_n)
    return pass_n + randText + passWord + randText + randText

# 取得したパスワードをファイル保存
def passWrite(passWord):
    # print('1',passWord)
    password111 = passHenge(passWord)
    with open(path + 'pass.txt', mode='w') as f:
        f.write(password111)

# def passReturn(passText):
#     # passWordを復号化
#     pass_n = int(passText[:2])-11
#     password = passText[36+2:36+2+pass_n]
#     return password


# root画面を作る
root = Tk()
root.title('パスワード登録')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

# パスワード表示
label2 = ttk.Label(frame1, text='Password', padding=(5, 2))
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
        exit(0)
        )
    )
button1.pack(side=LEFT)

# キャンセルボタンを作る
button2 = ttk.Button(frame2, text='キャンセル', command=exit)
button2.pack(side=LEFT)

root.mainloop()

