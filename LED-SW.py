from gpiozero import LED, Button 
import time

# LEDとスイッチのピン設定 
led = LED(17)     # GPIO #17をLEDに設定
sw = Button(6)    # GPIO #5をSWに設定

# LED点滅 
for  i  in  range(5):  # 5回繰り返す
     led.on() 
     time.sleep(0.5)   # 0.5秒待機
     led.off() 
     time.sleep(0.5) 

# スイッチ入力の監視 
print("スイッチの状態を監視します。Ctrl+Cで終了できます。") 
try: 
     while True:  # ずっと繰り返す
          if  not sw.is_pressed:
               print("スイッチが押されました！") 
          time.sleep(0.1) 
except KeyboardInterrupt:  # キーボードでCtrl+Cが入力されると以下を実行する
     print("終了します。")
