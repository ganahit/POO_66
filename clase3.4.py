# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:13:44 2025

@author: lab
"""
router=[]
lista=["R1","R2","R3","R4","S1","S2","S3",
       "AP1","AP2","AP3","FW1","FW2",
       "PC1","PC2","PC3"]
for item in lista:
    if "R" in item:
        router.append(item)
print(router)