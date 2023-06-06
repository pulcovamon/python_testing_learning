'''
Testing function, which finds the longest and shortest word in a given string.
'''
import pytest
from program.longest_and_shortest_word import shortest_and_longest_word

@pytest.mark.parametrize("test_input, expected", [
    ('A cow jumped over the moon.', ('A', 'jumped')),
    ('word', ('word', 'word')),
    ('   A cow jumped over    the  moon', ('A', 'jumped')),
    ('., ..? !!', None),
    ('', None)

])
def test_multiple_inputs(test_input, expected):
    assert shortest_and_longest_word(test_input) == expected

def test_with_invalid_input():
    with pytest.raises(TypeError):
        shortest_and_longest_word(123)

# Another possobility of pytest
@pytest.mark.xfail
def test_divide_by_zero():
    assert 1/0 == 1