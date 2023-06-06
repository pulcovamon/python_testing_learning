def shortest_and_longest_word(string_input:str)->tuple|None:
    """Returns the shortest and longest word in a given string.

    Args:
        string_input (str): text

    Returns:
        tuple: shortest and longest word
    """

    if not type(string_input) == str:
        raise TypeError('Input must be a string.')
    
    string_input = string_input.translate({ord(i): None for i in '.,?!'})
    string_input.strip()
    if not string_input:
        return None

    words = string_input.split()
    if not words:
        return None
    
    length = lambda word: len(word)
    words.sort(key=length)
    
    return words[0], words[-1]