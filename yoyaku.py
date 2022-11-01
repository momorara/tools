"""
講座予約

2022/11/01  開発開始

"""

import os
import sys
import getpass
import datetime
import time
import shutil
from tkinter import *
from tkinter import ttk


path = os.getcwd() + '/' # 現在のパスを取得
print(path)


# 排他処理
#　ファイルがあるか無いかを確認する。
if os.path.exists(path + 'lock.txt'):
    print('lockファィルがあった')
    # ゾンビ撃退 lockファイルの作成日時を取得
    locks_time = os.path.getmtime('./lock.txt')
    locks_date  = datetime.datetime.fromtimestamp(locks_time )
    print(locks_time,locks_date)
    # lockファィルが作成されてから10分以内ならプログラム停止
    if time.time() -locks_time < 600:
        # 使用中なのでメッセージを出し、プログラム終了
        # root画面を作る
        root = Tk()
        root.title('エラー')
        root.resizable(False, False)
        frame1 = ttk.Frame(root, padding=(32))
        frame1.grid()
        # 打刻してPC終了ボタンを作る
        button1 = ttk.Button(
            frame1, text='他の人が使用中です。', 
            command=lambda:(sys.ext())
            )
        button1.pack(side=LEFT)
        root.mainloop()

        pass
    else:
        # 10分以上経過なのでゾンビ認定、lockファイルを削除して継続
        os.remove(path + 'lock.txt') #ファイルを削除
else:
    # lockファイルがなかったので、使用中ではないと判断 lockファィルを作る
    with open(path + 'lock.txt', mode='w') as f: #上書き
        f.write(str('使用中'))


# 自分のいるフォルダ名を取得
# フォルダ名 os.path.dirname()
dir = os.path.dirname(path)
# print(dir) 
index =dir.rfind('/') +1
# print(index)
folderName = dir[index:]
print(folderName)
folderDir = dir[:index]
print(folderDir)

# userID取得
userID = getpass.getuser()
print(userID)

# hinaから掲示板をコピー　初回のみ
if not os.path.exists(path + 'reserveBoard.html'):
    # hinagataから掲示板をコピー
    print('html copy')
    shutil.copyfile(folderDir + 'hinagata/' + "reserveBoard.html", path + "reserveBoard.html")

# 掲示板表示
with open(path + "reserveBoard.html", mode='a') as f: #追記
    f.write('追記')

#------------ 処理関数 ------------------------
# 登録処理
def yoyaku():
    pass

# 削除処理
def sakujyo():
    pass


#---------------------------------------------

# 登録UI

# root画面を作る
root = Tk()
root.title('講座予約画面')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=2, column=1, sticky=W)


# 予約登録ボタンを作る
button1 = ttk.Button(
    frame2, text='予約登録', 
    command=lambda:( 
        yoyaku(),
        sys.exit())
    )
button1.pack(side=LEFT)


# 予約削除ボタンを作る
button2 = ttk.Button(
    frame2, text='削除', 
    command=lambda:( 
        sakujyo(),
        sys.exit())
    )
button2.pack(side=LEFT)


# キャンセルボタンを作る
button3 = ttk.Button(
    frame2, text='終了', 
    command=lambda:( 
        sys.exit())
    )
button3.pack(side=LEFT)

print('loopしてるのか?')

root.mainloop()



# 長時間稼働で終了

# 終了処理


