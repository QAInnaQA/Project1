from random import randint
from function import print_random

const_temp = 100_000

while True:

    var = int(input(' Fill number :'))

    if var == 1:
        print_random()

    if var == 2:
        print_random(var=var, additional_var=1)

    if var == 3:
        print_random(var=var)

    if not var:
        break

print('end of programm')
