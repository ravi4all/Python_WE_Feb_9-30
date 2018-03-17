Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,34,56,78,90]
>>> b = [10,20,30,40,50]
>>> a.append(b)
>>> a
[12, 34, 56, 78, 90, [10, 20, 30, 40, 50]]
>>> c = b
>>> c
[10, 20, 30, 40, 50]
>>> b
[10, 20, 30, 40, 50]
>>> id(c)
2139963890184
>>> id(b)
2139963890184
>>> c[0] = 'Bye'
>>> c
['Bye', 20, 30, 40, 50]
>>> b
['Bye', 20, 30, 40, 50]
>>> d = b[:]
>>> d
['Bye', 20, 30, 40, 50]
>>> b
['Bye', 20, 30, 40, 50]
>>> b[:]
['Bye', 20, 30, 40, 50]
>>> d[0] = 'Python'
>>> d
['Python', 20, 30, 40, 50]
>>> b
['Bye', 20, 30, 40, 50]
>>> c
['Bye', 20, 30, 40, 50]
>>> e = a[:]
>>> e
[12, 34, 56, 78, 90, ['Bye', 20, 30, 40, 50]]
>>> a
[12, 34, 56, 78, 90, ['Bye', 20, 30, 40, 50]]
>>> a[-1][0] = 'Hello'
>>> a
[12, 34, 56, 78, 90, ['Hello', 20, 30, 40, 50]]
>>> b
['Hello', 20, 30, 40, 50]
>>> c
['Hello', 20, 30, 40, 50]
>>> d
['Python', 20, 30, 40, 50]
>>> e
[12, 34, 56, 78, 90, ['Hello', 20, 30, 40, 50]]
>>> a[0] = 'Bye'
>>> s
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
['Bye', 34, 56, 78, 90, ['Hello', 20, 30, 40, 50]]
>>> b
['Hello', 20, 30, 40, 50]
>>> c
['Hello', 20, 30, 40, 50]
>>> e
[12, 34, 56, 78, 90, ['Hello', 20, 30, 40, 50]]
>>> import copy
>>> f = copy.deepcopy(a)
>>> f
['Bye', 34, 56, 78, 90, ['Hello', 20, 30, 40, 50]]
>>> a
['Bye', 34, 56, 78, 90, ['Hello', 20, 30, 40, 50]]
>>> a[-1][0] = 'Something'
>>> a
['Bye', 34, 56, 78, 90, ['Something', 20, 30, 40, 50]]
>>> e
[12, 34, 56, 78, 90, ['Something', 20, 30, 40, 50]]
>>> f
['Bye', 34, 56, 78, 90, ['Hello', 20, 30, 40, 50]]
>>> 
