Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pi=/
SyntaxError: invalid syntax
>>> pi=22/7
>>> print(pi)
3.142857142857143
>>> print("{:.2f}".format(pi))
3.14
>>> print("{:.7f}".format(pi))
3.1428571
>>> print("{:.60f}".format(pi))
3.142857142857142793701541449991054832935333251953125000000000
>>> hostnames=["R1","R2","R3","S1","S2"]
>>> type(hostnames)
<class 'list'>
>>> hostnames
['R1', 'R2', 'R3', 'S1', 'S2']
>>> hostnames[0]
'R1'
>>> hostnames[-1]
'S2'
>>> hostnames[0]="RTR1"
>>> hostnames
['RTR1', 'R2', 'R3', 'S1', 'S2']
>>> del hostnames[3]
>>> hotnames
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    hotnames
NameError: name 'hotnames' is not defined. Did you mean: 'hostnames'?
>>> hostnames
['RTR1', 'R2', 'R3', 'S2']
