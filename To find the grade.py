mark = int(input("Enter your mark:"))
if mark >= 1 and mark <= 100:
    if mark > 80:
        print("Grade A+")
    elif mark >= 70:
        print("Grade A")
    elif mark >= 60:
        print("Grade -A")
    elif mark >= 50:
        print("Grade B")
    elif mark >= 40:
        print("Grade C")
    elif mark >= 33:
        print("Grade D")
    else:
        print("F")
