#!/usr/bin/python3
"""
PROBLEM STATEMENT:
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each
denomination of coin in the list
Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    :param coins: list of the values of the coins in your possession
    :param total: the amount of money you want to make change for
    :return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """

    if total <= 0:
        return 0

    if len(coins) == 0:
        return -1

    coins.sort(reverse=True)
    num_count = 0
    for coin in coins:
        if total == 0:
            return num_count
        if total >= coin:
            num_count += total // coin
            total = total % coin
    if total == 0:
        return num_count
    return -1
