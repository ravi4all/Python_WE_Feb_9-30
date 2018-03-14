def temp_conv(c):
    return 9/5 * c + 32

temp = [33.4,35.4,32.6,36.5,38.2]

# for i in temp:
#     t = temp_conv(i)
#     print("Temperature is",t)

# Map
f = list(map(temp_conv, temp))
print(f)