"""
@author: TYZ
compute average word length
usage : input the list and output width, window increment. Output a list containing several
        lists which is a subset of input list and having a index increment by increment. Each
        list's width is equal to width.
"""


def slide_window(in_list, width, increment):
    """
    :param in_list: the input list
    :param width: output's list element width
    :param increment: the gap between 2 output list element
    :return: a list containing several lists which length = width, and each next list
             increments the first element's index in input list by increment.
             Those lists are all subsets to input list.
    """
    # check the input
    assert(width > 0 and increment > 0)
    assert(isinstance(in_list, list))

    length = len(in_list)
    cur_index = 0
    result = []

    if length < width:
        return result

    result.append(in_list[cur_index:cur_index+width])
    # while the window doesn't exceed the limit, increase and append
    while cur_index + increment <= length - width:
        cur_index += increment
        result.append(in_list[cur_index:cur_index + width])

    return result



