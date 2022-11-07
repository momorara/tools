"""
touroku_situation.py
現在募集中の掲示板を表示する。
by.kawabata

2folder化

基本データからnumber.htmlを持ってくること
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
os.chdir(path)
path = os.getcwd() + '/'
print('now       :',path)


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
folders.sort()
print(folders)

def html_read(html_path):
    try:
        with open(html_path,encoding="shift-jis") as f:
            htmlData = f.read()
    except:
        try:
            with open(html_path,encoding="cp932") as f:
                htmlData = f.read()
        except:
            with open(html_path,encoding="utf-8") as f:
                htmlData = f.read()
    return htmlData

def file_write(mesg):
    # htmlファイル更新
    with open(html_path, mode='a') as f:
        f.write(mesg)
        f.write("\n")

day_number = []
day_number_index = 0
for folder in folders:
    # ------------ 掲示板パス取得 ------------------------
    html_path = path + folder +'/reserveBoard.html' 
    print(html_path)

    # ------------ 掲示板を取得 ------------------------
    htmlData = html_read(html_path)   
 
    # ------------ 掲示板の申込数を取得 ------------------------                                            
    index1 = htmlData.find('_') # 申込人数の頭を探す
    index2 = htmlData.find('／') # 申込人数の頭を探す
    moushikomi = htmlData[index1+1:index2] # 
    print(moushikomi,day_number_index)
    day_number.append(moushikomi)
    day_number_index = day_number_index + 1
print(day_number)

# number.htmlパス
html_path = path +'number.html' 
print(html_path)


# number掲示板を作る
for i in range(len(folders)):
    print(folders[i],day_number[i])
    mesg = "<tr><td align=" + """left""" + ">" + "<font color=" + """blue""" + ">" + folders[i] + ':' + day_number[i] + "</font>" +  "</td></tr>"
    file_write(mesg)


# number.html表示
uri = 'file:///' + html_path
print(uri)
webbrowser.open_new(uri)
