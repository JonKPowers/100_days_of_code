from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = [word.strip() for word in f.read().split()]
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_score = sum([LETTER_SCORES.get(letter, 0) for letter in word.upper()])
    return word_score


def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY

    NOTE: If two words have an equal value, this function will return
    the first-occuring word in the list
    """

    max_word = None
    max_score = 0

    for word in word_list or load_words():
        word_value = calc_word_value(word)
        if  word_value > max_score:
            max_word = word
            max_score = word_value
    return max_word, max_score


if __name__ == "__main__":
    max_word, max_score = max_word_value()
    print(f'The highest Scrabble score is word: {max_word}. Score: {max_score}')
