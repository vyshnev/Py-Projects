#Fib upto the nth number

x= int(input("enter the nth number:"))

def fib_gen(x):
    a = 1
    b = 1
    for i in range(x):
        yield a
        a,b = b,a+b

for i in fib_gen(x):
    print(i)
