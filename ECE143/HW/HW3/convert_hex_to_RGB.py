"""
@author: TYZ
converting RGB hex_codes to RGB
usage : input the hex_list(eg:['#FFAAFF']) to function convert_hex_to_RGB,
        and the result will be a list of tuples containing the conversion of hex_codes to RGBs
"""


def convert_2char_to_2num(char1, char2):
    """
    :param char1: first char of single hex_code
    :param char2: second char of a single hex_code
    :return: conversion of hex_code to RGB

    Function design: convert_2char_to_2num the first char and the second char separately to nums, then add them together
    """
    if '0' <= char1 <= '9':
        """if the ascii value of char1 is between '0' and '9', then simply minus them to '0'"""
        num1 = ord(char1) - ord('0')
    elif 'A' <= char1 <= 'F':
        """else if the ascii value of char1 is above '9', add 10 to it after minus the ascii code of 'A'"""
        num1 = ord(char1) - ord('A') + 10
    else:
        """not valid input"""
        raise AssertionError("input not valid!")
    if '0' <= char2 <= '9':
        """if the ascii value of char2 is between '0' and '9', then simply minus them to '0'"""
        num2 = ord(char2) - ord('0')
    elif 'A' <= char2 <= 'F':
        """else if the ascii value of char2 is above '9', add 10 to it after minus the ascii code of 'A'"""
        num2 = ord(char2) - ord('A') + 10
    else:
        """not valid input"""
        raise AssertionError("input not valid!")

    """return the answer"""
    return num1 * 16 + num2


def convert_hex_to_RGB(hex_list):
    """
    :param hex_list: a list contains RGB hex_codes (eg: ['FFAAFF', 'FFAAFE'])
    :return: conversion of hex_codes to list of RGB number tuples

    Function design : convert_hex_to_RGB simply separate the hex_code to R,G,B and calculate the conversion of it. Then
    add them to a (R,G,B) tuple and push them to a list to generate the final result.
    """

    """the result lies in the RGB list"""
    RGB_list = []
    """the basic loop of extracting hex_codes from the hex_list"""
    for hex_codes in hex_list:
        """convert R,G,B separately using function convert_2char_to_2num"""
        if not (len(hex_codes) == 7 and hex_codes[0] == '#'):
            raise AssertionError("input not valid")
        RGB = (convert_2char_to_2num(hex_codes[1], hex_codes[2]), convert_2char_to_2num(hex_codes[3], hex_codes[4]),
               convert_2char_to_2num(hex_codes[5], hex_codes[6]))
        """then append the RGB number tuples to the RGB number tuple list"""
        RGB_list.append(RGB)

    """return the answer"""
    return RGB_list

