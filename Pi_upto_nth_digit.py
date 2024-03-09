# Print pi upto the nth digit
import decimal

checking = True
while checking:
    value = input('plase enter the nth value:')
    if not value.isdigit():
        print('please provide an integer')
        continue
    value= int(value)
    if value>100:
        print('Please provide the nth value less than or equal to 100')
        continue
    else:
        break
    
def pi_value(n):
    decimal.getcontext().prec= n+1
    pi = decimal.Decimal(22)/decimal.Decimal(7)
    print(f'the pi upto the {n}th precision point is {pi}')

pi_value(value)