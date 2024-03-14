#!/usr/bin/python3
"""
A module containing a function that checks if all boxes can be unlocked

You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked"""
    def update_current_keys(new_keys):
        """correctly updates current keys"""
        nonlocal current_keys
        current_keys.extend(new_keys)
        current_keys = list(set(current_keys))

    if len(boxes) <= 0:
        return True
    current_keys = []
    unlocked_boxes = set([0])
    update_current_keys(boxes[0])
    while current_keys:
        key = current_keys.pop(0)
        if key not in unlocked_boxes:
            unlocked_boxes.add(key)
            update_current_keys([x for x in boxes[key]
                                if x not in unlocked_boxes])
    if len(unlocked_boxes) == len(boxes):
        return True
    return False


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
