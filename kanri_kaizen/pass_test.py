"""
パスワード入力画面


PySimpleGUIをインストールしてください。
pip3 install pysimplegui


2022/10/30

"""

import random
import os

path = os.getcwd() + '/' # 現在のパスを取得
print(path)

def passHenge1(passWord):
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

def passReturn1(passText):
    # passWordを復号化
    pass_n = int(passText[:2])-11
    password = passText[36+2:36+2+pass_n]
    return password



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

# パスワードをファイル保存
def passWrite(passWord):
    # print('1',passWord)
    with open(path + 'pass.txt', mode='w') as f:
        f.write(passWord)

# 保存したパスワードを読込
def passRead():
    with open(path + 'pass.txt') as f:
        passWord = f.read()
    return passWord

def passget():
	passText = passRead()
	return passReturn(passText)
	
	
passW = 'kawabatatacanobu1234567890'
passW = 'Nobu4444_test123'
print(passW)

print('--1--')

passW = passHenge(passW)
print(passW)
passWrite(passW)
passW = 'xxx'

print('--2--')

passW = passRead()
print(passW)

print('--3--')

passW = passReturn(passW)
print(passW)

