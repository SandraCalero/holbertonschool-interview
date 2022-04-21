#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


from sqlalchemy import false


def canUnlockAll(boxes):
    if len(boxes) == 1 or len(boxes) == 0:
        return True
    isOpenList = [False] * (len(boxes) - 1)
    isOpenList[0] = True
    keyList = boxes[0]
    for key in keyList:
        if (key < len(isOpenList)) and (isOpenList[key] is False):
            isOpenList[key] = True
            keyList.extend(boxes[key])
    print(keyList)

    return all(isOpenList)
