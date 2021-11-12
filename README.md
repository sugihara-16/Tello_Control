# Tello_Control
### コマンド
- takeoff : 離陸
- land  : 着陸
- emergency : モーターが止まる
- fast_mode : 不明
- flattrim  : 不明
- palm_land : 機体の下に手を持ってくると、狙って着陸する模様
- throw_takeoff : 手から放ると飛ぶらしいが怖いので試してない
- type direction amount : 指定した方向に指定した量(cm, deg)動く
  - type = l or a (l = linear, a = angular)
  - direction = x or y or z (回転方向にx,yを入れたらどうなるのかは実験していない)
  - amount = float number
- flip direction  : フリップする
  - direction = 0 ~ 8 (時計回りに八等分したときの、大体の方向にflipする。flip 0だと12時の方向、flip 7　だと10.5時の方向)    
