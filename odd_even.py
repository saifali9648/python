def odd_even(number):
    if (number % 2) == 0:
        return 'even'
    else:
        return 'odd'

num=input('enter a number that you want to check that is even or odd:-')
result = odd_even(num)
print(result)