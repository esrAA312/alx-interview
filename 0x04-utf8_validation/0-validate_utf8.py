#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    Checks if a list of integers (data) is valid UTF-8 encoding
    """

    mask1 = 1 << 7
    mask2 = 1 << 6
    num_bytes = 0

    if not data or len(data) == 0:
        return True

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            while (mask & byte):
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    if num_bytes:
        return False
    else:
        return True
