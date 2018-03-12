Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str_1 = "Hello this is python"
>>> str_1[0]
'H'
>>> str_1[1]
'e'
>>> str_1[0:4]
'Hell'
>>> str_1[0:5]
'Hello'
>>> len(str_1)
20
>>> str_1[19]
'n'
>>> str_1[-1]
'n'
>>> str_1[-2]
'o'
>>> str_1[0:]
'Hello this is python'
>>> str_1[:20]
'Hello this is python'
>>> str_1[:10]
'Hello this'
>>> str_1[5:10]
' this'
>>> str_1[0:20:2]
'Hloti spto'
>>> x =
SyntaxError: invalid syntax
>>> x = "Shyam"
>>> reversed(x)
<reversed object at 0x000001601869B400>
>>> x[::-1]
'mayhS'
>>> str_1.capitalize()
'Hello this is python'
>>> str_1.upper()
'HELLO THIS IS PYTHON'
>>> str_1.lower()
'hello this is python'
>>> str_1.count('i')
2
>>> str_1.find('o')
4
>>> str_1.rfind('o')
18
>>> str_2 = "Hello world this is python programming"
>>> str_2.find('o')
4
>>> str_2.rfind('o')
29
>>> str_2.rfind('o',4)
29
>>> str_2.rfind('o',1)
29
>>> str_2.rfind('o',5)
29
>>> str_2.find('o',4)
4
>>> str_2.find('o',5)
7
>>> str_2.find('o',8)
24
>>> str_2.split()
['Hello', 'world', 'this', 'is', 'python', 'programming']
>>> str_1[0] = 'B'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    str_1[0] = 'B'
TypeError: 'str' object does not support item assignment
>>> str_1.replace('Hello', 'Bye')
'Bye this is python'
>>> str_1
'Hello this is python'
>>> 
