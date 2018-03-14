def calc(x,y):
    yield x+y
    yield x-y
    yield x/y
    yield x*y
    print("This is a generator")

res = calc(12,3)
# print(next(res))

for output in res:
    print(output)