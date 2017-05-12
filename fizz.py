num = 0

while num < 100:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz {0}'.format(num))
    elif num % 5 == 0:
        print('Buzz {0}'.format(num))
    elif num % 3 == 0:
        print('Fizz {0}'.format(num))
    num += 1
