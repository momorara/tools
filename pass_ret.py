"""
パスワード復号
tkinterで作成

2022/10/30

"""
import os

path = os.getcwd() + '/' # 現在のパスを取得
print(path)

def passRead():
    with open(path + 'pass.txt') as f:
        passWord = f.read()
    return passWord

def passReturn(passText):
    # passWordを復号化
    pass_n = int(passText[:2])-11
    password = passText[36+2:36+2+pass_n]
    return password


text = passRead()
result = passReturn(text)
print(result)
