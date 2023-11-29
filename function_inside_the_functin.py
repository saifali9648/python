def get_name():
    name=input('enter your name:-')
    return name
def say_name(name):
    print('your name is {}.'.format(name))

def get_show_name():
    """get the name and display name"""
    name=get_name()
    say_name(name)
get_show_name()
