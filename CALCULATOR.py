while True:
    a = int(input("Enter a :"))
    b = int(input("Enter b :"))
    cal = input("What do you want to do? (+,-,*,/):")

    if cal == '+':
        print(a+b)
    elif cal == '-':
        print(a-b)
    elif cal == '*':
        print(a*b)
    elif cal == '/':
        if b == 0 :
            print("It's not possible!")
        else:    
            print(a/b)
    ask = input("Do you want to try again?")
    if ask == 'n':
        break
