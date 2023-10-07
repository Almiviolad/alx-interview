#!/usr/bin/python3
"""module contains function that determine if all thr lockboxes can opened"""


def canUnlockAll(boxes):
    """Arg: boxes-an list of boxes
       return: True if all the boxes can be opened and False otherwise"""
    if not boxes:
        return False

    opened = set()
    stack = [0]
    while stack:
        box = stack.pop()
        opened.add(box)
        for key in boxes[box]:
            if key not in opened and key < len(boxes):
                stack.append(key)
    return len(boxes) == len(opened)
