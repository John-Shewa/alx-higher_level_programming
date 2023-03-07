#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = repr(number)
lastdigit_str = last_digit[-1]
lastdigit = int(lastdigit_str)
if lastdigit > 5:
    print('Last digit of', number, 'is', lastdigit, 'and is greater than 5\n')
elif lastdigit == 0:
    print('Last digit of', number, 'is', lastdigit, 'and is 0\n')
elif lastdigit < 6 and lastdigit != 0:
    print ('Last digit of', number, 'is', lastdigit, 'and is less than 6 and not 0\n')
