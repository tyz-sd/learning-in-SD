"""
@author: TYZ
simply judging whether the number is less than 9 and greater than 0.
"""


def is_string_integer(char_input):
    """
    :param char_input: a single char input
    :return: a boolean meaning whether the char input is an integer
    """
    return (char_input <= '9') and (char_input >= '0')

