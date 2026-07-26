"""
*
**
***
****
*****
"""

def pattern(current,target):
    if current > target:
        return
    print(current*"*")
    pattern(current+1,target)
pattern(1,5)

"""
*****
****
***
**
*
"""

def pattern(n):
    if n == 0 :
        return
    print("*"*n)
    pattern(n-1)
pattern(6)
