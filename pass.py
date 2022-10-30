"""
パスワード入力画面


PySimpleGUIをインストールしてください。
pip3 install pysimplegui


2022/10/30

"""
import PySimpleGUI as sg
import os

path = os.getcwd() + '/' # 現在のパスを取得
print(path)

layout = [  [sg.Text('パスワードを入力')],    
            [sg.Input()],
            [sg.Button('決定'), sg.Button('キャンセル')]]

window = sg.Window('sample', layout)

event, values = window.read()

window.close()

print(f'eventは{event}')
print(f'valuesは{values}')
print(values[0])

if event == '決定':
    with open(path + 'pass.txt', mode='w') as f: #上書き
        f.write(str(values[0]))


