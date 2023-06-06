'''
Learnign testing using this tutorial:
https://realpython.com/python-testing/

funtion for trying tests
'''

def sum_of_mine(numbers:list|tuple)->int|float:
    """add any number of numbers

    Args:
        numbers (list|tuple of int|floats): numbers

    Returns:
        int|float: sum of the given numbers
    """
    result = 0
    for number in numbers:
        result += number
    return result

if __name__ == '__main__':
    print(sum_of_mine([1, 2, 3]))