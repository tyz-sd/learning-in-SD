"""
@author: TYZ
compute average word length
usage : input the instring(type of 'str') and a unique flag(indicating whether multiple
        words should be counted as one).
"""


def compute_average_word_length(instring, unique=False):
    """
    :param instring: the input string, it's type should be str.
    :param unique: the input flag, indicates whether multiple words should be counted
    :return: the average word length of parsed content.

    Function design: First split the input string using delimiter as ' ' and '\n'. Then
                     turn it into set if the unique flag is True. Finally, calculate the
                     average length.
    """

    # assert the input to be a string
    assert(isinstance(instring, str))

    if unique:
        parsed = set(instring.replace('\n', ' ').split(' '))
        parsed = [i for i in parsed if i != '']
        result = sum([len(i) for i in parsed])/len(parsed)
    else:
        parsed = instring.replace('\n', ' ').split(' ')
        parsed = [i for i in parsed if i != '']
        result = sum([len(i) for i in parsed])/len(parsed)

    return result


