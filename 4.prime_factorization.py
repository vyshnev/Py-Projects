
from sympy import primefactors  #sympy is an external library in python used in symbolic mathematics. its an important library 

def main():
    try:
        num = int(input("enter the number:"))
        if num<2:
            print("please enter a value more than 1")
        else:
            factors = primefactors(num)
            if len(factors) == 1:
                print(f"the number {num} is a prime number")
            else:
                print(f"the factors of {num} are:{', '.join(map(str,factors))}")

    
    except:
        print("Please enter a vaild number")


factorize = main()  #usually we assign the function to a variable, but here we dont have to do that as factorize is not
                    #returning anything. So if we call main() directly its still correct
