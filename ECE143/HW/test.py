"""
@author: ZTY
* generate test cases to test HW:
    * Each testcase will be identified.
"""

# HW1 : is string integer:
import HW1.is_string_integer as HW1_F
# HW2 : compute area rectangle
import HW2.compute_area_rectangle as HW2_F
# HW3 : convert hex to RGB
import HW3.convert_hex_to_RGB as HW3_F
# HW4 : compute average word length
import HW4.compute_average_word_length as HW4_F
# HW6 : slide window
import HW6.slide_window as HW6_F

if __name__ == "__main__":

    # HW1 : is string integer
    string1 = " "
    string2 = "1"
    string3 = "a"
    string4 = "\n"
    res = [HW1_F.is_string_integer(string1), HW1_F.is_string_integer(string2), HW1_F.is_string_integer(string3),
            HW1_F.is_string_integer(string4)]

    print(res)

    # HW2 : compute area rectangle
    """
    input1 = ['1.1', '1.2', '1.1', '1.2']
    input2 = ['1', '1', '1', '1']
    input3 = ['1', '2', '1', '2']
    input4 = ['-1', '2', '-1', '2']
    input5 = ['1', '2', '1', '3']
    try:
        res = HW2_F.compute_area_rectangle(input1)
    except AssertionError as E:
        print(E.args)
        pass
    else:
        print(res)

    try:
        res = HW2_F.compute_area_rectangle(input2)
    except AssertionError as E:
        print(E.args)
        pass
    else:
        print(res)

    try:
        res = HW2_F.compute_area_rectangle(input3)
    except AssertionError as E:
        print(E.args)
        pass
    else:
        print(res)

    try:
        res = HW2_F.compute_area_rectangle(input4)
    except AssertionError as E:
        print(E.args)
        pass
    else:
        print(res)

    try:
        res = HW2_F.compute_area_rectangle(input5)
    except AssertionError as E:
        print(E.args)
        pass
    else:
        print(res)
    """


    # HW3 : convert hex to RGB
    hex_codes = ['#FFAABB', '#F998AB', '#DFFAAD']
    RGBs = HW3_F.convert_hex_to_RGB(hex_codes)
    print(RGBs)


    # HW4: compute average word length
    print(HW4_F.compute_average_word_length("Mary had a little lamb\n\
    its fleece was white as snow\n\
    and everywhere that Mary went\n\
    the lamb was sure to go", False))

    ##HW6: slide window
    print(HW6_F.slide_window([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 3))
