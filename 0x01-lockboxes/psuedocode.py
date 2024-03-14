def canUnlockAll(boxes):
    let boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    let current_keys = set([])
    add boxes[0] to current keys
    (boxes 0 contain 1, 4, 6)
    remove 0 from current keys and add to used keys
    add boxes[1], boxes[4], boxes[6] to current keys
    unlocked = [0, 1, 4, 6]
    repeat process until len of boxes iterations and determine if boxes can be unlocked
    
    ----------testing------------
    1,4,6
    1,
    4, 6, 2
    4,
    6, 2, 3
    6,
    2, 3
    2,
    3
    3,
    5, 
    5,


    [0,1,4,6]
    

    ----------testing------------
    [[1], [2], [3], [4], []]
    1
    2
    3
    4
