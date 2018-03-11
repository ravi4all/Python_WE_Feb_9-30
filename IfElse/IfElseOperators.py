Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = a > 5
>>> b
True
>>> b = a < 5
>>> b
False
>>> b = a > 5 and a < 15
>>> b
True
>>> b = a > 5 or a < 9
>>> b
True
>>> b = a > 5 || a < 9
SyntaxError: invalid syntax
>>> b = a > 5 | a < 9
>>> b
False
>>> b = a > 5 & a < 9
>>> b
True
>>> a
10
>>> a = ['Hello', 'Hi', 'Bye', 'Yes', 'No']
>>> 'No' in a
True
>>> 'Hie' not in a
True
>>> a = 12
>>> b = 5
>>> result = "A is greater" if a > b else "B is Greater"
>>> result
'A is greater'
>>> result = "Even number" if a % 2 == 0 else "Odd number"
>>> result
'Even number'
>>> 
