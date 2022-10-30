"""
退勤時確認画面


PySimpleGUIをインストールしてください。
pip3 install pysimplegui


2022/10/30

"""

import PySimpleGUI as sg
import os


layout = [  [sg.Text('退勤処理を選択してください。')],    
            [sg.Button('打刻してPC終了'), sg.Button('打刻せずPC終了'), sg.Button('キャンセル')]]

window = sg.Window('sample', layout)
event, values = window.read()
window.close()

print(f'eventは{event}')

