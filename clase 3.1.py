# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 09:34:06 2025

@author: lab
"""
aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
    print("This is a extended IPv4 ACL. ")
else:
    print("This is not a standar  a extended IPv4 ACL. ")
