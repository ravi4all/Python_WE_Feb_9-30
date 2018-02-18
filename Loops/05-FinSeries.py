# Fib Series - 0 1 1 2 3 5 8 13 21 34

num = 1
series = 0

while series < 100:
    print(series, end=' ')
    num, series = series, num + series
##    num = series
##    series = num + series
