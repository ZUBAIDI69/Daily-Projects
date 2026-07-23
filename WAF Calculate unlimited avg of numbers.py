def avg ():
    i = 0
    sum_avg = 0
    while True:
        a = int(input("Enter Your number:"))
        if a == 0 :
            average = sum_avg/i
            print(average)
        sum_avg += a
        i += 1
avg()
    
