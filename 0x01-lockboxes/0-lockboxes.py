#!/usr/bin/python3
"""
Unlock boxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each inner list
        represents a box and contains keys to unlock other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    total_keys = set(boxes[0]) | {0}  # Initialize with keys from 1st box(box0)
    added = True

    while added:
        added = False
        for box_keys in boxes:
            for key in box_keys:
                if key not in total_keys:
                    total_keys.add(key)
                    added = True

    return len(total_keys) == len(boxes)
