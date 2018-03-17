Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,34,45,67,78]
>>> a = (12,34,45,67,78)
>>> type(a)
<class 'tuple'>
>>> a[0]
12
>>> a[0:3]
(12, 34, 45)
>>> a[-1]
78
>>> a[0] = 'Hi'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[0] = 'Hi'
TypeError: 'tuple' object does not support item assignment
>>> emp = 'Ram', 27, 25000
>>> emp
('Ram', 27, 25000)
>>> a = 10,
>>> a
(10,)
>>> name,age,sal = 'Ram', 27, 56000
>>> name
'Ram'
>>> age
27
>>> sal
56000
>>> emp = name,age,sal = 'Ram', 27, 56000
>>> emp
('Ram', 27, 56000)
>>> age
27
>>> sal
56000
>>> name
'Ram'
>>> 
