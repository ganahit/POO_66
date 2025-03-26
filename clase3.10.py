# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:51:59 2025

@author: lab
"""
while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
x=int(x)
y=1
while  True:
    print(y)
    y=y+1
    if y>x:
        break