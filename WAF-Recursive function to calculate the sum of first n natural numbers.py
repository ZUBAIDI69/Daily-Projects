def Sum(n):
    if n==0:
        return 0
    return Sum(n-1)+n
cal_sum = Sum(5)
print(cal_sum)
