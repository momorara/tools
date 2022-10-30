"""
退勤時確認画面
tkinterで作成

2022/10/30

"""
from tkinter import *
from tkinter import ttk



def dakoku_end():
    print('打刻してPC終了')

def no_dakoku_end():
    print('打刻せずPC終了')


# root画面を作る
root = Tk()
root.title('退勤処理選択')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=2, column=1, sticky=W)


# 打刻してPC終了ボタンを作る
button1 = ttk.Button(
    frame2, text='打刻してPC終了', 
    command=lambda:( 
        dakoku_end(),
        exit(0)
        )
    )
button1.pack(side=LEFT)


# 打刻せずPC終了ボタンを作る
button2 = ttk.Button(
    frame2, text='打刻せずPC終了', 
    command=lambda:( 
    no_dakoku_end(),
    exit(0)
    )
    )
button2.pack(side=LEFT)


# キャンセルボタンを作る
button3 = ttk.Button(
    frame2, text='キャンセル', command=exit)
button3.pack(side=LEFT)


root.mainloop()