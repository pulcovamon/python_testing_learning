'''
I am using this tutorial:
https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/

This is simple function for learning testing.
'''

def formatted_name(first_name, last_name, middle_name=''):
    """Combines first name and last name

    Args:
        first_name (str)
        last_name (str)
    """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

if __name__ == '__name__':
    print('Enter first and last name or enter x to exit.')

    while True:
        first_name = input('First name: ')
        if first_name == 'x':
            print('Good bye.')
            break

        last_name = input('First name: ')
        if last_name == 'x':
            print('Good bye.')
            break

    result  = formatted_name(first_name, last_name)
    print(result)