#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    isOpenList = [False] * (len(boxes) - 1)
    isOpenList[0] = True
    keyList = boxes[0]
    for key in keyList:
        if (key < len(boxes)) and (isOpenList[key] is False):
            isOpenList[key] = True
            keyList.extend(boxes[key])

    return all(isOpenList)
