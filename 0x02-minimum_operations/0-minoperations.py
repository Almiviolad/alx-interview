#!/usr/bin/python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
 Copy All and Paste.
Given a number n, write a method that
calculates the fewest number of operations
 needed to result in exactly n H characters in the file

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0"""


def minOperations(n):
    """calculates fewest operation to get n Char(H)"""
    if n < 1:
        return 0

    operations = 0
    no_of_H = 1
    clipboard = 0

    while no_of_H < n:
        if n % no_of_H == 0:
            clipboard = no_of_H
            operations += 2  # copy all and paste operations
        else:
            operations += 1  # paste
        no_of_H += clipboard
    return operations
