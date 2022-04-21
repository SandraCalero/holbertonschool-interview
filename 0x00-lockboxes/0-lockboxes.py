#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    check = False
    if len(boxes) == 0:
        return True
    index_list = [boxes.index(box) for box in boxes]
    index_list[0] = 'Open'
    for box in boxes:
        check = all(box == index_list[0] for box in index_list)
        if check:
            return True
        if box == [] and check == False:
            return False
        for key in box:
            if key in index_list and index_list[key] != 'Open':
                index_key = index_list.index(key)
                index_list[index_key] = 'Open'
