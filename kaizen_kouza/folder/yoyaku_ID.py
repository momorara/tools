"""
講座予約

2022/11/01  開発開始
2022/11/02	html表示

"""


import webbrowser
import os
import sys
import getpass
import datetime
import time
import shutil
from tkinter import *
from tkinter import ttk
import subprocess


# ------------ 環境確認 ------------------------
path = os.getcwd() + '/'  # 現在のパスを取得
print(path)

print('step1')

# 自分のいるフォルダ名を取得
# フォルダ名 os.path.dirname()
dir = os.path.dirname(path)
print('dir:', dir)
# index =dir.rfind("kaizen_kouza") +13
# index =dir.rfind('\') +1
index = dir.rfind('\\') + 1  # バックスラッシュの検索はややこしいね。
# print('index:',index)
folderName1 = dir[index:]
print('folderName1:', folderName1)
folderDir1 = dir[:index]
print('folderDir1:', folderDir1)

folderDir2 = folderDir1[:-1]
print('folderDir2:', folderDir2)
index = folderDir2.rfind('\\') + 1
# print('index:',index)
folderName2 = folderDir2[index:]
print('folderName2:', folderName2)

# userID取得
userID = getpass.getuser()
print('userID:', userID)

# hinaから掲示板をコピー　初回のみ
if not os.path.exists(path + 'reserveBoard.html'):
    # hinagataから掲示板をコピー
    # print(folderDir1)
    # print('html copy',folderDir1)
    shutil.copyfile(
    folderDir1 +
    'hinagata\\' +
    "reserveBoard.html",
    path +
     "reserveBoard.html")
    # YYYMMDDを当該日付に変更
    with open(path + 'reserveBoard.html') as f:
        htmlData = f.read()
    htmlData = htmlData.replace('YYYYMMDD', folderName1)
    with open(path + 'reserveBoard.html', mode='w') as f:  # 上書き
        f.write(htmlData)


# ------------ 掲示板表示 ------------------------
uri = 'file:///' + path + 'reserveBoard.html'
print(uri)
webbrowser.open_new(uri)
# webbrowser.open_new_tab(uri)


# ------------ 処理関数 ------------------------
# ファイル更新処理
def file_write(mesg):
	# ロックファイルがあるか無いかを確認する。# 排他処理
    while os.path.exists(path + 'lock.txt'):
        print('lockファィルがあった')
        # ゾンビ撃退 lockファイルの作成日時を取得
        locks_time = os.path.getmtime('./lock.txt')
        locks_date = datetime.datetime.fromtimestamp(locks_time)
        print(locks_time, locks_date)
        # lockファィルが作成されてから３秒以内ならプログラム待機
        if time.time() - locks_time < 3:
            # 使用中なのでメッセージを出し、プログラム待機
            # root画面を作る
            root = Tk()
            root.title('エラー')
            root.resizable(False, False)
            frame1 = ttk.Frame(root, padding=(32))
            frame1.grid()
            label2 = ttk.Label(frame1, text='他の人が使用中です。', padding=(5, 2))
            label2.grid(row=1, column=0, sticky=E)
            root.mainloop()
        else:
            # 5秒以上経過なのでゾンビ認定、lockファイルを削除して継続
            print('ゾンビ認定')
            try:
                os.remove(path + 'lock.txt')  # ファイルを削除
            except:
                pass
    # ロックファイル作成
    with open(path + 'lock.txt', mode='w') as f:
        f.write(str('使用中'))
    # 登録ファイル更新
    with open(path + 'reserveBoard.html', mode='a') as f:
        f.write(mesg)
        f.write("\n")
    # 排他処理解除
    os.remove(path + 'lock.txt') #ファイルを削除


def tel_number_check(tel_number):
    # tel_numberは文字列で来る
    print(type(tel_number),tel_number)
    try:
        tel = int(tel_number)
    except:
        tel = 0
    if tel > 9999 or tel < 1000 : # あり得ない番後の時は-1
        tel = -1
    return tel


# 登録処理
def yoyaku(tel_number):
    tel = tel_number_check(tel_number)
    if tel != -1 :
        mesg = "<tr><td align=" + """left""" + ">" + "<font color=" + """blue""" + ">" + "_+" + userID + "</font>#" + "menber" + "</td></tr>"
        #mesg2 = "<script>var element = document.documentElement;var bottom = element.scrollHeight - element.clientHeight;window.scroll(0, bottom);</script>"
        file_write(mesg)
    else:# 内線番号がおかしい場合
        # root画面を作る
        root = Tk()
        root.title('エラー')
        root.resizable(False, False)
        frame1 = ttk.Frame(root, padding=(32))
        frame1.grid()
        label2 = ttk.Label(frame1, text='内線番号がおかしいです。', padding=(5, 2))
        label2.grid(row=1, column=0, sticky=E)
        root.mainloop()


# 削除処理
def sakujyo():
    mesg = "<tr><td align=" + """right""" + ">" + "<font color=" + """red""" + ">" + "_-" + userID + "</font>#" + "menber" + "</td></tr>"
    file_write(mesg)


# データ整理し有効予約数を計算
#------------ ユニークな要素のみにし、登録から削除を消す ------------------------
# 対象文字列を探す。
def data_seiri():
	with open(path + 'reserveBoard.html') as f:
		htmlData = f.read()
	touroku = []
	index = htmlData.find('_+') # 登録を探す
	while index != -1:
		touroku.append(htmlData[index+2:index+8])
		#print(htmlData[index+2:index+8])
		index = index +10
		index = htmlData.find('_+',index)
	print(len(touroku),touroku)
	# ユニークな要素だけにする
	touroku = list(dict.fromkeys(touroku))
	print(len(touroku),touroku)

	sakujo = []
	index = htmlData.find('_-') # 削除を探す
	while index != -1:
		sakujo.append(htmlData[index+2:index+8])
		#print(htmlData[index+2:index+8])
		index = index +10
		index = htmlData.find('_-',index)
	# ユニークな要素だけにする
	sakujo = list(dict.fromkeys(sakujo))
	print('削除',sakujo)

	# 登録から削除を消す
	#print(len(sakujo))
	if len(sakujo) >0 :
		for i in range(len(sakujo)):
			valueToBeRemoved = sakujo[i]
			touroku = [value for value in touroku if value != valueToBeRemoved]
	print(len(touroku),touroku)
	
	# 掲示板の申込数を更新
	index1 = htmlData.find('_') # 申込人数の頭を探す
	index2 = htmlData.find('／') # 申込人数の頭を探す
	moushikomi = htmlData[index1:index2] # 
	print(index1,index2,moushikomi)
	moushikomi_new = "_申込" + str(len(touroku)) + "名"
	htmlData = htmlData.replace(moushikomi,moushikomi_new)
	with open(path + 'reserveBoard.html', mode='w') as f: #上書き
		f.write(htmlData)


#--------------------UI作成-------------------------
print('step2')
# 登録UI

# root画面を作る
root = Tk()
root.title('講座予約画面')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

# パスワード表示
label2 = ttk.Label(frame1, text='内線番号を入力後、予約登録してください。', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

# 内線番号入力フレームを作る
tel_number = StringVar()
tel_number_entry = ttk.Entry(
    frame1,
    textvariable=tel_number,
    width=20)
tel_number_entry.grid(row=1, column=1)


frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=2, column=1, sticky=W)


# 予約登録ボタンを作る
button1 = ttk.Button(
    frame2, text='予約登録', 
    command=lambda:(
        yoyaku(tel_number.get()),data_seiri()))
button1.pack(side=LEFT)

# 予約削除ボタンを作る
button2 = ttk.Button(
    frame2, text='削除', 
    command=lambda:(sakujyo(),data_seiri()))
button2.pack(side=LEFT)
#command=lambda:(sakujyo(),sys.exit()))


# キャンセルボタンを作る
button3 = ttk.Button(
    frame2, text='終了', 
    command=lambda:(sys.exit()))
button3.pack(side=RIGHT)

print('loopしてるのか?')

root.mainloop()



# 長時間稼働で終了

# 終了処理

