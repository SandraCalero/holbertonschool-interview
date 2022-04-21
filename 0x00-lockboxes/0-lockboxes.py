#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


from sqlalchemy import false


def canUnlockAll(boxes):
    if len(boxes) == 1 or len(boxes) == 0:
        return True
    if boxes[0] == [0] or boxes[0] == [] or boxes[0] >= len(boxes):
        return False
    index_list = [False for box in boxes]
    index_list[0] = True
    isOpen = False
    for box in boxes:
        for key in box:
            if key < len(index_list):
                if index_list[key] is False:
                    index_list[key] = True
            isOpen = all(index_list)
            if isOpen:
                return True
            if box == [] and isOpen is False:
                return False
            if boxes.index(box) == len(index_list) - 1 and isOpen is False:
                return False
