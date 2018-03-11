Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list_1 = [10,12,14,30,40,55,60]
>>> list_1 = [10,12,14,30,40,55,60,'ten','tweleve','bye'10.5]
SyntaxError: invalid syntax
>>> list_1 = [10,12,14,30,40,55,60,'ten','tweleve','bye',10.5]
>>> list_1[0]
10
>>> list_1[1]
12
>>> len(list_1)
11
>>> list_1[10]
10.5
>>> list_1[-1]
10.5
>>> list_1[-2]
'bye'
>>> list_1[0:5]
[10, 12, 14, 30, 40]
>>> list_1[4:9]
[40, 55, 60, 'ten', 'tweleve']
>>> list_1[0:10:2]
[10, 14, 40, 60, 'tweleve']
>>> list_1[0:10:3]
[10, 30, 60, 'bye']
>>> list_1[::-1]
[10.5, 'bye', 'tweleve', 'ten', 60, 55, 40, 30, 14, 12, 10]
>>> list_1[:]
[10, 12, 14, 30, 40, 55, 60, 'ten', 'tweleve', 'bye', 10.5]
>>> list_1[::]
[10, 12, 14, 30, 40, 55, 60, 'ten', 'tweleve', 'bye', 10.5]
>>> list_1[::-1]
[10.5, 'bye', 'tweleve', 'ten', 60, 55, 40, 30, 14, 12, 10]
>>> list_1[:-1]
[10, 12, 14, 30, 40, 55, 60, 'ten', 'tweleve', 'bye']
>>> data = []
>>> user_data = []
>>> user_data.append('Ram')
>>> user_data
['Ram']
>>> user_data.append('Sam')
>>> user_data.append('Lucky')
>>> user_data.append('John')
>>> user_data
['Ram', 'Sam', 'Lucky', 'John']
>>> user_data.append('Delhi','NY','Agra','UK')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    user_data.append('Delhi','NY','Agra','UK')
TypeError: append() takes exactly one argument (4 given)
>>> for i in range(4):
	city = input("Enter city : ")
	user_data.append(city)

	
Enter city : Delhi
Enter city : NY
Enter city : Agra
Enter city : UK
>>> user_data
['Ram', 'Sam', 'Lucky', 'John', 'Delhi', 'NY', 'Agra', 'UK']
>>> user_data.pop()
'UK'
>>> user_data
['Ram', 'Sam', 'Lucky', 'John', 'Delhi', 'NY', 'Agra']
>>> user_data.pop()
'Agra'
>>> del user_data[1]
>>> user_data
['Ram', 'Lucky', 'John', 'Delhi', 'NY']
>>> user_data.pop(1)
'Lucky'
>>> user_data
['Ram', 'John', 'Delhi', 'NY']
>>> for i in range(4):
	city = input("Enter city : ")
	user_data.append(city)

	
Enter city : Patna
Enter city : Mumbai
Enter city : Chennai
Enter city : Pune
>>> user_data
['Ram', 'John', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune']
>>> user_data.index('Mumbai')
5
>>> user_data.insert(2,'Lucky')
>>> user_data
['Ram', 'John', 'Lucky', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune']
>>> user_data[0] = 'Laxman'
>>> user_data
['Laxman', 'John', 'Lucky', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune']
>>> age = [23,24,25]
>>> user_data.extend(age)
>>> user_data
['Laxman', 'John', 'Lucky', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune', 23, 24, 25]
>>> companies = ['HCL','TCS','Wipro']
>>> user_data.append(companies)
>>> user_data
['Laxman', 'John', 'Lucky', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune', 23, 24, 25, ['HCL', 'TCS', 'Wipro']]
>>> user_data = []
>>> names = []
>>> 
>>> names = ['Ram','Shyam','Arjun']
>>> city = ['Delhi','Pune','Mumbai']
>>> companies = ['HCL','TCS','Wipro']
>>> user_data.append(name)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    user_data.append(name)
NameError: name 'name' is not defined
>>> user_data.append(names)
>>> user_data.append(city)
>>> user_data.append(companies)
>>> user_data
[['Ram', 'Shyam', 'Arjun'], ['Delhi', 'Pune', 'Mumbai'], ['HCL', 'TCS', 'Wipro']]
>>> user_data[0]
['Ram', 'Shyam', 'Arjun']
>>> user_data.pop()
['HCL', 'TCS', 'Wipro']
>>> user_data
[['Ram', 'Shyam', 'Arjun'], ['Delhi', 'Pune', 'Mumbai']]
>>> user_data.append(companies)
>>> user_data[0]
['Ram', 'Shyam', 'Arjun']
>>> user_data[0][0]
'Ram'
>>> user_data[0].append('John')
>>> user_data
[['Ram', 'Shyam', 'Arjun', 'John'], ['Delhi', 'Pune', 'Mumbai'], ['HCL', 'TCS', 'Wipro']]
>>> user_data_1 = ['Laxman', 'John', 'Lucky', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune', 23, 24, 25, ['HCL', 'TCS', 'Wipro']]
>>> user_data_1.remove('John')
>>> user_data_1 = ['Laxman', 'John', 'Lucky', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune','John', 23, 24, 25, 'John']
>>> user_data_1.remove('John')
>>> user_data_1
['Laxman', 'Lucky', 'Delhi', 'NY', 'Patna', 'Mumbai', 'Chennai', 'Pune', 'John', 23, 24, 25, 'John']
>>> 
