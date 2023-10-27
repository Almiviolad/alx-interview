#!/usr/bin/python3
"""Write a method that determines if a given data set
 represents a valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you
 only need to handle the 8 least significant bits of each integer"""


def validUTF8(data):
    """determines if a given data set\
 represents a valid UTF-8 encoding"""
    bytes_to_read = 0
    for num in data:
        if bytes_to_read == 0:
            if num >> 7 == 0b0:
                bytes_to_read = 0

            elif (num >> 5 == 0b110):
                # 2  bytes
                bytes_to_read = 1

            elif (num >> 4 == 0b1110):
                # 3 bytes
                bytes_to_read = 2
            elif (num >> 3 == 0b11110):
                bytes_to_read = 3
            else:
                return False
        else:
            if (num >> 6 != 0b10):
                return False
            bytes_to_read -= 1
    return bytes_to_read == 0
