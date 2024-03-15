import mpmath


while True:
    n = int(input("Enter the number of digits you want after the decimal point: "))
    if n> 100:
        print('Limit exceeded: Please provide digit not more than 100:')
        continue
    break
        

def find_e_to_nth_digit(n):
    mpmath.mp.dps= n+2          #this provides the digit to n precision
    e = mpmath.e                #this is used to provide the e value
    print (str(e)[:n+2])        #to print e to the nth value


find_e_to_nth_digit(n)
