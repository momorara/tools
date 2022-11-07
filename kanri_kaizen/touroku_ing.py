
"""
touroku_ing.py
現在募集中の掲示板を表示する。
by.kawabata

2folder化
"""
import os
import time
import webbrowser
import copy


kouza_folder_name = 'kaizen_kouza'
kanri_folder_name = 'kanri_kaizen'


# ------------ 環境確認 ------------------------
path = os.getcwd() + '/'
print('path      :',path)
os.chdir('..')
path_kouza = os.getcwd() + '/' + kouza_folder_name+ '/'
path_kanri = os.getcwd() + '/' + kanri_folder_name+ '/'
print('path_kanri:',path_kanri)
print('path_kouza:',path_kouza)
os.chdir(path_kanri)
path = os.getcwd() + '/'
print('now       :',path)



# 同一パスにあるフォルダー(dir)のみリスト化する
files = os.listdir(path_kouza)
folders = [f for f in files if os.path.isdir(os.path.join(path_kouza, f))]
# print(folders)    # ['dir1', 'dir2']
# 20220101以上の数字フォルダだけにする
# AM,PNM対応する
folders_cp = copy.copy(folders)
for folder in folders_cp:
    # 文字か数字か判定　数字で20220101以上なら 1
    flag = 0
    folder_int = folder[:8]
    #print('**',folder_int)
    if str.isdigit(folder_int):
        folder_int = int(folder_int)
        if int(folder_int) >20220100:
            flag = 1
    if flag == 0:
        folders.remove(folder)
print(folders)

for folder in folders:
    # ------------ 掲示板表示 ------------------------
    uri = 'file:///' + path_kouza + folder +'/reserveBoard.html' 
    print(uri)
    webbrowser.open_new(uri)
