def greet():
    print("hello!")
    print("welcome to python")
greet()

def add(a,b):
    answer = a+b
    print("the answer is:",answer)
add (10,20)

def sub(a,b):
    answer = a-b
    print("the is is:",answer)
sub(10,20)

def multi(a,b):
    answer = a*b
    print("the answer is:",answer)
multi(10,20)

def div(a,b):
    answer = a/b
    print("the answer is:",answer)

def check__even__odd(number):
    if number%2==0:
        print(number, "is Even") 
    else:
        print(number, "is odd")
    check__even__odd(8)    
    check__even__odd(7)   