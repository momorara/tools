"""
gpio_gui02.py

2020/12/01  gpioの状態を表示する。
2020/12/02  gpio readallから各gpioの状態を配列に取得
2021/03/20  ピンの設定がoutだと入力できないので、全てのピンを入力に設定する。
    02      その際の注意も表示


PySimpleGUIをインストールしてください。
pip3 install pysimplegui

scp -r ../exp pi@172.20.10.2:/home/pi
scp -r ../exp/gpio_gui.py pi@172.20.10.2:/home/pi/exp
"""
import RPi.GPIO as GPIO
import PySimpleGUI as sg
import subprocess 

pos1 = [12,12,0,1,2,13,14,11,10,9,8,10,14,15,2,3,16,4,4,16,17,18,6,6,7,9,17,5]
pos2 = [0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0]

def res_cmd(cmd):
  return subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]

def gpio_get(gpio):
  cmd = ("gpio readall")
#   gpio_readall_b = res_cmd(cmd)
  gpio_readall = res_cmd(cmd).decode()
  for i in range(0,28):
    gpio[i] = gpio_readall[352+80*pos1[i]+15*pos2[i]:353+80*pos1[i]+15*pos2[i]]

def gpio_input():
    pin = 1
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for i in range(27):
        GPIO.setup(pin,GPIO.IN)
        pin = pin + 1 

def main():

    #  セクション1 - 最初の注意事項ダイアログ
    layout = [
        [sg.Text('gpio_gui02.py 注意事項')],
        [sg.Text('全てのピンを入力設定にします。', size=(30, 1))],
        [sg.Text('', size=(30, 1)),],
        [sg.Submit(button_text='実行ボタン')]
    ]

    window = sg.Window("gpio 入力状態を確認", layout,resizable=True, size=(250,150))

    while True:
        event, values = window.read()
        print(event, values)
        if event=='GO - Lチカ':
            pass
        else:
            break
    window.close()


    #  セクション2 - gpioを全てinputに設定して、状態を表示

    gpio_input()

    gpio = [i for i in range(0, 28)]
    update_text = [i for i in range(0, 28)]
    gpio_get(gpio)
    # print(gpio)

    layout = [
        [sg.Text('更新周期 ms'),sg.Slider(range=(100,5000), default_value =500, resolution=100, orientation='h', size=(100, None),key="cycle")],

        [sg.Text('GPIO #0 = 0',key='-gpio0-'),sg.Text('   '),sg.Text('GPIO #1 = 1',key='-gpio1-')],
        [sg.Text('GPIO #2 = 2',key='-gpio2-'),sg.Text('   '),sg.Text('GPIO #3 = 3',key='-gpio3-')],
        [sg.Text('GPIO #4 = 4',key='-gpio4-'),sg.Text('   '),sg.Text('GPIO #5 = 5',key='-gpio5-')],
        [sg.Text("GPIO #6 = 6",key="-gpio6-"),sg.Text('   '),sg.Text("GPIO #7 = 7",key="-gpio7-")],
        [sg.Text("GPIO #8 = 8",key="-gpio8-"),sg.Text('   '),sg.Text("GPIO #9 = 9",key="-gpio9-")],
        [sg.Text("GPIO #10 = 10",key="-gpio10-"),sg.Text(''),sg.Text("GPIO #11 = 11",key="-gpio11-")],
        [sg.Text("GPIO #12 = 12",key="-gpio12-"),sg.Text(''),sg.Text("GPIO #13 = 13",key="-gpio13-")],
        [sg.Text("GPIO #14 = 14",key="-gpio14-"),sg.Text(''),sg.Text("GPIO #15 = 15",key="-gpio15-")],
        [sg.Text("GPIO #16 = 16",key="-gpio16-"),sg.Text(''),sg.Text("GPIO #17 = 17",key="-gpio17-")],
        [sg.Text("GPIO #18 = 18",key="-gpio18-"),sg.Text(''),sg.Text("GPIO #19 = 19",key="-gpio19-")],
        [sg.Text("GPIO #20 = 20",key="-gpio20-"),sg.Text(''),sg.Text("GPIO #21 = 21",key="-gpio21-")],
        [sg.Text("GPIO #22 = 22",key="-gpio22-"),sg.Text(''),sg.Text("GPIO #23 = 23",key="-gpio23-")],
        [sg.Text("GPIO #24 = 24",key="-gpio24-"),sg.Text(''),sg.Text("GPIO #25 = 25",key="-gpio25-")],
        [sg.Text("GPIO #26 = 26",key="-gpio26-"),sg.Text(''),sg.Text("GPIO #27 = 27",key="-gpio27-")],

        [sg.Button('End.',size=(15,2),border_width=8), sg.Button('Cancel')] ,
        [sg.Text('注) 更新周期の単位はmsです。')],
    ]

    window = sg.Window("GPIO 状態表示", layout,resizable=True, size=(300,540))
    cycle = 500
    while True:
        event, values = window.read(timeout=cycle,timeout_key='-timeout-')
        print(event, values)
        if event=='-timeout-':
            gpio_get(gpio)
            for i in range(0,28):
                update_text[i] = 'GPIO #' + str(i) + ' = ' + str(gpio[i])
                win = '-gpio' + str(i) + '-'
                print(win)
                window[win].update(update_text[i])
            cycle = int(values["cycle"])
        else:
            break
    window.close()

if __name__ == '__main__':
  main()

