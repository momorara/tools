"""
ＴＦＴ液晶の性能評価

文字の大きさと色を変えてアルファベットを表示
abcdefghijklmnopqrstuvqxyz
abcdefghijklmnopqrst
abcdefghijklmnop

lcd177_0.py の　DISP_rotationを0,90,180,270で変更すると表示向きを変えられる

2024/02/10  ターミナルプロックの位置に対応するプログラムの整理
"""
import lcd177_0
import time

def main():

    lcd177_0.init('on')

    mes= 'abcdefghijklmnopqrstuvqxyz'
    print(mes)
    lcd177_0.disp(mes,12,'white')

    mes= 'abcdefghijklmnopqrst'
    lcd177_0.disp(mes,16,'blue')

    mes= 'abcdefghijklmnop'
    lcd177_0.disp(mes,20,'red')

    mes= 'abcdefghijklm'
    lcd177_0.disp(mes,24,'green')

    mes= 'abcdefghijk'
    lcd177_0.disp(mes,28,'white')

    time.sleep(2)
    lcd177_0.init('off')
    lcd177_0.init('reset')

if __name__ == "__main__":
    main()
