# -*- coding: utf-8 -*-
num = int(input('何番目までのフィボナッチ数を表示しますか？整数で入力してください : '))

a, b = 0, 1
for i in range(0,num):
  print(b)
  a, b = b, a + b
  if b == num:
    break
