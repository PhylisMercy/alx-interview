#!/usr/bin/python3
"""
    UTF-8 Validation
"""


def validUTF8(data):
    """ Validate UTF-8 Encodings """
    num_bytes = 0
    for num in data:
        num = format(num, '#010b')[-8:]

        # start of new char
        if num_bytes == 0:
            num_bytes = get_byte_count(num)-1
            if num_bytes is None:
                return False

        # continue processing char
        else:
            if not num.startswith("10"):
                return False
            num_bytes -= 1

    return num_bytes == 0


def get_byte_count(num):
    """ Get byte count of character """
    prefix_dict = {
        "0": 1,
        "110": 2,
        "1110": 3,
        "11110": 4,
        }

    for prefix in prefix_dict:
        if num.startswith(prefix):
            return prefix_dict[prefix]

    return False
