#!/usr/bin/python
# 
"""
2024/09/14  AB Shutter3 シャッターボタンの確認
            ボタンの押下でevent.val 1 手放しでevent.val 0 を確認
            押している間の判定ができる。
            ボタンをしばらく使わないと省電力のためか接続が切れる
            再度接続するには電源の切り入りが必要
2024/09/17  一度trustまでしていると
            ABでもCWでも、自動的に繋がりますね。
        
"""
import evdev
import time

while True:
    try:
        # ls /dev/input でevent番号要確認
        device = evdev.InputDevice('/dev/input/event5')
        print(device)

        for event in device.read_loop():
            print("event",event)
            print("type",type(event))
            print("event.code",event.code)
            print("event.val",event.value)
            print("event.type ",event.type )

            if event.code == 115:
                  print("event.val",event.value)
                  
    except:
        print('Retry...')
        time.sleep(1)