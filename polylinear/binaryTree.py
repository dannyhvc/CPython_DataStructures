from typing import (
    Any,
    overload
)
from enum import Enum
from dataclasses import dataclass

# class type proto
_BinaryTreeNode = object
BinaryTree = object

#%%
class WorkingStatus(Enum):
    OK = 0
    STALE = 1
    FAILED = -1


@dataclass
class _BinaryTreeNode:
    Parent: _BinaryTreeNode = None
    Left: _BinaryTreeNode = None
    Right: _BinaryTreeNode = None
    Data: Any = None


@dataclass
class BinaryTree:
    root: _BinaryTreeNode = None
    size: int = 0


def insert(val: Any, master: BinaryTree) -> None:
    '''
    insert
    ------
    Inserts value into tree following the
    #### params:
        + val (Any): any data to be help within the node
    #### returns:
        + None
    '''
    if master._size == 0:
        master.root = _BinaryTreeNode()
        master.root.data = val
        master.size += 1
    else:
        _insert(val, master.root)


def _insert(val: Any, node: _BinaryTreeNode):
    '''
    _insert
    --------
    '''
    status: WorkingStatus = WorkingStatus.FAILED
    try:
        if node is None:
            node = _BinaryTreeNode()
            node.data = val
            node.size += 1
            status = WorkingStatus.OK
        else:
            if val < node.Data:
                _insert(val, node.Left)
            elif val > node.Data:
                _insert(val, node.Right)
            else:
                # reject if the node is equal
                status = WorkingStatus.STALE
    except Exception as insertExcept:
        print(insertExcept)
        status = WorkingStatus.FAILED
    return status


if __name__ == '__main__':
    bt = BinaryTree()
    print(bt)
