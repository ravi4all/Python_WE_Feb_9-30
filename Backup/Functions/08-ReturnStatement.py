def calc(x,y):
    return x+y, x-y, x/y, x*y

# result = calc(12,44)
# print(result)

# add, sub, div, mul = calc(44,12)
# print(add,sub,div,mul)

a,b,*c = calc(44,12)
print(a,b,c)