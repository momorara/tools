"""
現在募集中の掲示板を表示する。
by.kawabata

2folder化
"""
import os
import time
import webbrowser
import copy


kouza_folder_name = 'kaizen_kouza'


# ------------ 環境確認 ------------------------
path = os.getcwd() + '/'
print(path)
os.chdir('..')
path1 = os.getcwd() + '/' + kouza_folder_name+ '/'
print(path1)
os.chdir(path1)
path = os.getcwd() + '/'
print(path)

# 同一パスにあるフォルダー(dir)のみリスト化する
files = os.listdir(path)
folders = [f for f in files if os.path.isdir(os.path.join(path, f))]
# print(folders)    # ['dir1', 'dir2']
# 20220101以上の数字フォルダだけにする
folders_cp = copy.copy(folders)
for folder in folders_cp:
    # 文字か数字か判定　数字で20220101以上なら 1
    flag = 0
    if str.isdigit(folder):
        folder_int = int(folder)
        if int(folder) >20220100:
            flag = 1
    if flag == 0:
        folders.remove(folder)
print(folders)

for folder in folders:
    # ------------ 掲示板表示 ------------------------
    uri = 'file:///' + path + folder +'/reserveBoard.html' 
    print(uri)
    webbrowser.open_new(uri)

