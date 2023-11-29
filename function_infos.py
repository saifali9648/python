def say_hi(name):
    print('hi {}'.format(name))
    
say_hi('saif')
say_hi('everyone')

#this is the example of default parameter
def say_hi(name='there'):
    print(' hi {}'.format(name))

say_hi()
say_hi('saif')

#example of multiple paramerter

def say_hi(fname,lname):
    print('  hi {},{}'.format(fname,lname))
    
say_hi('jhon','deo')
say_hi('saif','ali')

def say_hi(fname,lname):
    '''say hello'''
    print('  hi {},{}'.format(fname,lname))
    
help(say_hi)


#program of odd even number

def get_odd_even(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

num = int(input('enter a number that you want to check that number is odd or enen:-'))
result=get_odd_even(num)
print(result)