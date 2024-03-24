import sympy


def nxt_prime():
    a = 0
    while True:
        user_input = input("do you want the next prime number(Y/N):").lower()
        if user_input == 'y':
            a = sympy.nextprime(a)
            print (a)
            continue
        elif user_input == 'n':
            print("exiting the programme")
            break
        else:
            print("Input as either Y or N")


prime = nxt_prime()