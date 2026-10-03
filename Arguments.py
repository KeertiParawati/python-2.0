def total__calc(bill__amount,tip__perc):
    total = bill__amount*(1+0.01*tip__perc)
    total = round(total,2)
    print(f"Please pay${total}")
total__calc(150,20) 


def cube(number):
     return number*number*number
def by__three(number):
    if number %3==0:
        return cube (number)
    else:
     return False        
print(by__three(9))
print(by__three(4))


def factorial(x):
    if x == 0 or x == 1:
     return 1
    else:
       return x*factorial(x-1)
print("the factorial of 0:" ,factorial(0))
print("the factorial of 1:" ,factorial(1))
print("the factorial of 2:" ,factorial(2))
print("the factorial of 5:" ,factorial(5))
print("the factorial of 10:" ,factorial(10))