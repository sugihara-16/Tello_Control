# Tello_Control
### コマンド
- takeoff 離陸
- land  着陸
- emergency モーターが止まる
- fast_mode 
- flattrim
- palm_land
- throw_takeoff
- type direction amount 
  - type = l or a (l = linear, a = angular)
  - direction = x or y or z (回転方向にx,yを入れたらどうなるのかは実験していない)
  - amount = float number
- flip direction
  - direction = 0 ~ 8 (時計回りに八等分したときの、大体の方向にflipする。flip 0だと12時の方向、flip 7　だと10.5時の方向)    
