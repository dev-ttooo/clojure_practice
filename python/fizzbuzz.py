# -*- coding: utf-8 -*-
num = int(input("正の整数を入力してください:"))
for i in range(1, num):
    if i % 15 == 0:
        print("Fizz Buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)