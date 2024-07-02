#!/usr/bin/python3
"""
Module 
"""


def canUnlockAll(boxes):
    """
    Function 
    """
    # Number of boxes
    n = len(boxes)

    eeunlocked = set()
    eeunlocked.add(0)

    stack = [0]

    while stack:
        c_box = stack.pop()

        for key in boxes[c_box]:
            if key < n and key not in eeunlocked:
                eeunlocked.add(key)
                stack.append(key)

    return len(eeunlocked) == n
