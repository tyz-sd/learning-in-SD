"""
@author TYZ
A simple calculator evaluates the area of a rectangle(except square)
"""


def compute_area_rectangle(length, width):
    """
    :param length: the length of the rectangle.
    :param width: the width of the rectangle.
    :return: the area of given rectangle. One double value
    """

    # check if a rectangle
    if length <= 0 or width <= 0:
        raise AssertionError("input is not a valid rectangle - side length less equal than 0")

    if length == width:
        raise AssertionError("input is not a valid rectangle - this is a square")

    # calculate S

    return length * width




