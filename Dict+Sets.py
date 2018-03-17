Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> emp = {'name':'John', 'age':22, 'country':'US'}
>>> type(emp)
<class 'dict'>
>>> emp[1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    emp[1]
KeyError: 1
>>> emp['name']
'John'
>>> emp = {'name':['Ram','Shyam','Sam','Mike'], 'company' : ['HCL','TCS','Wipro','Infy']}
>>> emp
{'name': ['Ram', 'Shyam', 'Sam', 'Mike'], 'company': ['HCL', 'TCS', 'Wipro', 'Infy']}
>>> emp['name']
['Ram', 'Shyam', 'Sam', 'Mike']
>>> emp['name'][2]
'Sam'
>>> emp = [{'name':'Ram', 'company':'HCL'},{'name':'Shyam','company':'TCS'}]
>>> emp
[{'name': 'Ram', 'company': 'HCL'}, {'name': 'Shyam', 'company': 'TCS'}]
>>> emp[0]
{'name': 'Ram', 'company': 'HCL'}
>>> emp[0]['name']
'Ram'
>>> set_1 = {2,3,4,5,6}
>>> set_2 = {5,2,8,9,1}
>>> set_1 & set_2
{2, 5}
>>> set_1 | set_2
{1, 2, 3, 4, 5, 6, 8, 9}
>>> set_1.intersection(set_2)
{2, 5}
>>> x = [2,4,5,3,1,2,7,8,9,5,6,3]
>>> set(x)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> str_1 = "Hello this is python programming and python is used for machine learning"
>>> str_2 = "Machine learning is so popular today and python programming is also very popular"
>>> str_1 = str_1.split(" ")
>>> str_1
['Hello', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> str_2 = str_2.split(" ")
>>> stopwords = ['is','am','are','the','for','also','and','this','that','so']
>>> set_1 = set(str_1)
>>> set_2 = set(str_2)
>>> set_3 = set(set_3)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set_3 = set(set_3)
NameError: name 'set_3' is not defined
>>> 
>>> set_3 = set(stopwords)
>>> set_1
{'machine', 'is', 'programming', 'Hello', 'and', 'used', 'python', 'for', 'learning', 'this'}
>>> set_2
{'Machine', 'is', 'and', 'programming', 'so', 'popular', 'today', 'python', 'learning', 'also', 'very'}
>>> set_3
{'am', 'is', 'and', 'so', 'for', 'that', 'the', 'this', 'also', 'are'}
>>> set_1.intersection(set_3)
{'and', 'for', 'is', 'this'}
>>> str_token_1 = []
>>> for word in str_1:
	if word not in stopwords:
		str_token_1.append(word)

		
>>> str_token_1
['Hello', 'python', 'programming', 'python', 'used', 'machine', 'learning']
>>> str_token_2 = []
>>> for word in str_2:
	if word not in stopwords:
		str_token_2.append(word)

		
>>> str_token_2
['Machine', 'learning', 'popular', 'today', 'python', 'programming', 'very', 'popular']
>>> 
