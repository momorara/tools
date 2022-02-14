raspberry pi tool


#ラズベリーパイ向けのツールを置いておきます。
git clone https://github.com/momorara/tools
でダウンロード

ip_get_MakeFile.py
    自分のipアドレスを取得しipアドレス名のファイルを作る

cpustat.py

　　cpuの現在の状態(使用状況、温度)をレポートします。
  
info.py

　　ラズパイの機種、cpi使用率、cpu温度を表示します。
 　*複数のラズパイを使い、sshでログインしていると、どのラズパイに居るか分からなくなるので、
  　ただし、同じ機種を使っているとわからないけどね。
   *本当はログインネームを変えるべきだけど、それだと面倒なので...
   
LED_gui02.py -.sh

　　Lチカ支援ツール
  
gpio_gui02.py -.sh
   
　　gpioの状態を確認するツール
  
gui使うには以下をインストールしてください。
pip3 install pysimplegui
  
  
