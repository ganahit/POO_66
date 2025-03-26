# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:16:40 2025

@author: lab
"""
router=[]
switch=[]
Ap=[]
Fw=[]
Tv=[]
Ipt=[]
varios=[]
lista=["R1","R2","R3","R4","S1","S2","S3",
       "AP1","AP2","AP3","FW1","FW2",
       "PC1","PC2","PC3","TV1","TV2","IPT1","IPT2","pSP1","pSP2"]
for item in lista:
    if "R" in item:
        router.append(item)
    elif "S" in item:
        switch.append(item)
    elif "AP" in item:
        Ap.append(item)
    elif "FW" in item:
        Fw.append(item)
    elif "TV" in item:
        Tv.append(item)
    elif "IPT" in item:
        Ipt.append(item)
    else:
        varios.append(item)

print(router)
print(switch)
print(Ap)
print(Fw)
print(Tv)
print(Ipt)
print(varios)
