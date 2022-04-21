#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    isOpen = [False] * len(boxes)
    isOpen[0] = [True]
    keyList = boxes[0]
    for key in keyList:
        if ((key < len(boxes)) and (isOpen[key] is False)):
            isOpen[key] = True
            keyList.extend(boxes[key])
    return all(isOpen)
