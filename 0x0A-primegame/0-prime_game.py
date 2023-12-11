#!/usr/bin/python3
""" determines winner of prime game"""


def isPrime(n):
    """checks if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def remove(array, num):
    """removes num and multiples"""
    return [n for n in array if n % num != 0]


def isWinner(x, nums):
    """determines winner of prime game"""
    wins = {'Maria': 0, 'Ben': 0}

    for n in nums[:x]:
        numArray = list(range(n + 1))
        # print(numArray)
        count = 0

        for num in numArray[:]:  # Create a copy of the list to iterate over
            # print(numArray)
            if isPrime(num):
                numArray = remove(numArray, num)
                count += 1
        # print(count)

        winner = 'Ben' if count % 2 == 0 else 'Maria' if count > 0 else None
        if winner:
            wins[winner] += 1

    if wins['Maria'] == wins['Ben']:
        return None

    return max(wins, key=wins.get)
