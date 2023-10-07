#!/usr/bin/python3
"""module contains function that determine if all thr lockboxes can opened"""


def canUnlockAll(boxes):
    """Arg: boxes-an list of boxes
       return: True if all the boxes can be opened and False otherwise"""
    if boxes[0] != []:
        avail_keys = []
        boxNo = len(boxes)
        for key in boxes[0]:
            avail_keys.append(key)
        i = 0
        for key in avail_keys:
            current = boxes[avail_keys[i]]
            for key_no in current:
                if key_no not in avail_keys and key_no != 0 and key_no < boxNo:
                    avail_keys.append(key_no)
            i = i + 1
        if boxNo == len(avail_keys) + 1:
            return (True)
        else:
            return (False)
    if boxNo > 1 or boxNo == 0:
        return (False)
    return (True)
