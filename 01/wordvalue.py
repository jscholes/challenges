from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        words = f.readlines()
    return [word.rstrip('\n') for word in words]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = word.upper()
    return sum([LETTER_SCORES[letter] for letter in word])

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate
