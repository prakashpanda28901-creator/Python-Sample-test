def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(num1,num2):
    if num2==0:
        raise ValueError("cannot divided by zero")
    return num1/num2