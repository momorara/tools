"""
LED_gui02.py

2020/11/29  gui Lチカ GPIO No,回数をキーボード入力
2020/11/30
    01      マウスのみの操作でできるUIとする。
2020/12/21  バグ改修
2021/03/20  ピンの設定がoutだと入力できないので、全てのピンを入力に設定する。
    02      その際の注意も表示
    
PySimpleGUIをインストールしてください。
pip3 install pysimplegui

scp -r exp/*.py pi@192.168.68.126:/home/pi/exp
scp -r exp pi@192.168.68.126:/home/pi

"""
import PySimpleGUI as sg
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#  セクション1 - 最初の注意事項ダイアログ
layout = [
    [sg.Text('LED_gui02.py 注意事項')],
    [sg.Text('使用するピンは出力設定します。', size=(30, 1))],
    [sg.Text('なので、200Ω以下の抵抗でプルアップ、プルダウンしていると', size=(60, 1))],
    [sg.Text('ラズパイを壊す可能性があります。', size=(30, 1)),],
    [sg.Text('', size=(30, 1)),],
    [sg.Text('そこのところ、注意よろしくです!!', size=(30, 1)),],
    [sg.Text('', size=(30, 1)),],
    [sg.Text('', size=(30, 1)),],
    [sg.Submit(button_text='実行ボタン')]
]

window = sg.Window("Lチカ支援", layout,resizable=True, size=(450,280))

while True:
    event, values = window.read()
    print(event, values)
    if event=='GO - Lチカ':
        pass
    else:
        break
window.close()

#  セクション2 - LEDチカチカ

layout = [
   [sg.Text('GPIO # '),sg.Slider(range=(0,27), default_value =26, resolution=1, orientation='h', size=(100, None),key="-GPIO-")],
   [sg.Text('点滅回数'),sg.Slider(range=(1,30), default_value =3, resolution=1, orientation='h', size=(100, None),key="-NN-")],
   [sg.Text('')],
   [sg.Text('点灯時間'),sg.Slider(range=(0.1,1), default_value =0.1, resolution=0.1, orientation='h', size=(100, None),key="-ON-")],
   [sg.Text('消灯時間'),sg.Slider(range=(0.1,1), default_value =0.1, resolution=0.1, orientation='h', size=(100, None),key="-OFF-")],
   [sg.Text('')],
   [sg.Button('GO - Lチカ',size=(15,2),border_width=8), sg.Button('Cancel')] ,
   [sg.Text('')],
   [sg.Text('注) GPIOがHigtで点灯設定です。')],
]

window = sg.Window("Lチカ支援", layout,resizable=True, size=(300,350))

while True:
    event, values = window.read()
    print(event, values)
    if event=='GO - Lチカ':
        LEDPIN  = int(values["-GPIO-"])
        NN      = int(values["-NN-"])
        ON_time = values["-ON-"]
        OFF_time= values["-OFF-"]
        print(LEDPIN,NN,ON_time,OFF_time)
        GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO. LOW)
    
        for i in range(NN):
                GPIO.output(LEDPIN,GPIO.HIGH)
                time.sleep(ON_time)
                GPIO.output(LEDPIN,GPIO.LOW)
                time.sleep(OFF_time)
    else:
        break
    
window.close()
GPIO.cleanup()
    