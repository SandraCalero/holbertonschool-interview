#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    if len(boxes) == 0:
        return True
    index_list = [False for box in boxes]
    index_list[0] = True
    isOpen = False
    for box in boxes:
        isOpen = all(index_list)
        if isOpen:
            return True
        if box == [] and isOpen is False:
            return False
        for key in box:
            if index_list[key] is not True:
                index_list[key] = True
