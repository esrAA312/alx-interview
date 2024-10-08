#!/usr/bin/python3
""" this file contains a script"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    """

    if total <= 0:
        return 0

    coins_count = 0
    reste = total
    idx = 0
    sorted_list_coins = sorted(coins, reverse=True)
    n = len(coins)
    while reste > 0:
        if idx >= n:
            return -1
        if reste - sorted_list_coins[idx] >= 0:
            reste -= sorted_list_coins[idx]
            coins_count += 1
        else:
            idx += 1
    return coins_count
