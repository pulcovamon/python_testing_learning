'''
Learnign basics of automation testing with python.
I am using this video: https://www.youtube.com/watch?v=tGzyAoVU1Ks
'''

def vowel_count(string_input):
    """Counts number of vowels in a given string.

    Args:
        string_input (str): text

    Returns:
        int: number of vowels
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for character in string_input.lower():
        if character in vowels:
            count += 1

    return count
    

def test_with_my_name():
    assert vowel_count('monika pulcova') == 6

def test_with_my_uppercase_name():
    assert vowel_count('MONIKA PULCOVA') == 6


'''
Challange 01: Write more tests
'''

def test_with_numbers():
    assert vowel_count('123456') == 0

def test_with_special_characters():
    assert vowel_count('!@#$%^&*()') == 0

def test_with_empty_string():
    assert vowel_count('') == 0

def test_with_only_vowels():
    assert vowel_count('aeiou') == 5

def test_with_only_consonants():
    assert vowel_count('bcdfghjklmnpqrstvwxyz') == 0

def test_with_vowels_and_consonants():
    assert vowel_count('aeioubcdfghjklmnpqrstvwxyz') == 5

'''
Challange 02: A new function
    Write a function that takes a string and returns
    the shortest and longes word within it.

    'A cow jumped over the moon.'

    Write tests -> assert that function works as expected
'''

def shortest_and_longest_word(string_input):
    """Returns the shortest and longest word in a given string.

    Args:
        string_input (str): text

    Returns:
        tuple: shortest and longest word
    """

    if not type(string_input) == str:
        raise TypeError('Input must be a string.')
    
    string_input = string_input.translate({ord(i): None for i in '.,?!@#$%^&*()-'})
    string_input.strip()
    if not string_input:
        return None

    words = string_input.split()
    if not words:
        return None
    
    length = lambda word: len(word)
    words.sort(key=length)
    
    return words[0], words[-1]

def test_with_sentence():
    assert shortest_and_longest_word('A cow jumped over the moon.') == ('A', 'jumped')

def test_with_one_word():
    assert shortest_and_longest_word('word') == ('word', 'word')

def test_with_blank_spaces():
    assert shortest_and_longest_word('   A cow jumped over    the  moon') == ('A', 'jumped')

def test_with_special_characters():
    assert shortest_and_longest_word('#$%^A cow!!! jumped, @over@ the? moon.') == ('A', 'jumped')

def test_with_only_special_characters():
    assert shortest_and_longest_word('.,?!@ #$% ^&*()-') == None

def test_with_empty_string():
    assert shortest_and_longest_word('') == None

def test_with_integer():
    try:
        shortest_and_longest_word(123)
        assert False
    except TypeError:
        assert True

def test_with_list():
    try:
        shortest_and_longest_word(['a', 'b', 'c'])
        assert False
    except TypeError:
        assert True
