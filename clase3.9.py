# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:48:06 2025

@author: lab
"""
x=input("Enter a number to count to:")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    if y>x:
        break
