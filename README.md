raspberry pi tool


#ラズベリーパイ向けのツールを置いておきます。

LED-Checker組立説明書v1.pdf
その名の通りです。


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


*上記プログラムは素人作成なので、環境により動作しない場合もあります。
質問や要望がありましたら　フェイスブックの
寝屋川 電子工作工房(主にラズパイ)
https://www.facebook.com/groups/3773038759434230
"Raspberry Pi Japan"でお願いします。
*上記プログラムを使用しての不具合等については一切責任を持ちませんので、よろしくお願いします。
  
