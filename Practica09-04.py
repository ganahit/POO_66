# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:15:50 2025

@author: lab
"""
class Employee:
    empCount = 0
    def __init__(self,name, salary):
        Employee.empCount +=1
        def displayCount(self):
            print ("Total Employee %d", Employee.empCount)
        def displayEmployee(self):
            print("Name : ", self.name, "Salary: ",self.salary)
empleado1=Employee("Jefferson", 800)
empleado2=Employee("Genesis", 850)
empleado3=Employee("Said",700)
print("Total Employee %d" % Employee.empCount)
