import os

current_dir = os.getcwd()
print("Before",current_dir)

os.chdir('C:/Users/asus/FullMachineLearning/ML_CaseStudies/EmailSpam/emails')

current_dir = os.getcwd()
print("After",current_dir)

path = current_dir
# print(os.walk(path))
for i,j,k in os.walk(path):
    # print(i)
    # print(j)
    print(k)

# os.system()