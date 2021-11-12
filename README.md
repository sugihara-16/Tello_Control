# Tello_Control
### コマンド
基本的に、tello_driverがsubscribeしている同名のトピックに、入力情報を流し込んでいる(位置調整は例外)。
- takeoff : 離陸
- land  : 着陸
- emergency : モーターが止まる
- fast_mode : 不明
- flattrim  : 不明
- palm_land : 機体の下に手を持ってくると、狙って着陸する模様
- throw_takeoff : 手から放ると飛ぶらしいが怖いので試してない
- type direction amount : 指定した方向に指定した量(cm, deg)動く。(例 l x 20 →右方向に20cm直進)
  - type = l or a (l = linear, a = angular)
  - direction = x or y or z (回転方向にx,yを入れたらどうなるのかは実験していない)
  - amount = float number
- flip direction  : フリップする
  - direction = 0 ~ 8 (時計回りに八等分したときの、大体の方向にflipする。flip 0だと12時の方向、flip 7　だと10.5時の方向)    
 
### 問題点
- どのコマンドも、動いたり動かなかったりする。1,2回打ち込めば大体反応するが、flipに関しては何回やっても動かないことがある(これは、電池残量が少ないとそうなるのかも)
  - telloへのソケット通信の周波数と、tello_driverの周波数がずれているのかもしれない？
- tello_driverには、速度を調整するtopic(tello/cmd_vel)しか用意されていない。そのため位置を制御するには、あらかじめ速度を一定値に決めておき、入力された変位量に応じて移動時間を制御する必要がある。
  - それでも、変位量を大きくしていくと精度がかなり落ちてしまう。
 
