"""
@author: Daniel Herrera-Vazquez
"""
from dataclasses import dataclass
from typing import Any, Optional, NewType

DeNode: type = NewType('DeNode', object)
DeList: type = NewType('DeList', object)


@dataclass
class DeNode:
    Next: Optional[DeNode] = None
    Prev: Optional[DeNode] = None
    Data: Optional[Any] = None


@dataclass
class DeList:
    Head: Optional[DeNode] = None
    Tail: Optional[DeNode] = None
    Size: int = 0


def is_empty(dell: DeList) -> bool:
    return dell.Size == 0


def push_back(val: Any, dell: DeList) -> None:
    temp: DeNode = DeNode(val)
    if is_empty(dell):
        # filling first node in empty list
        dell.Head = dell.Tail = temp
        dell.Head.Next = dell.Tail
        dell.Tail.Prev = dell.Head
    else:
        dell.Tail.Next = temp
        dell.Tail.Next.Prev = dell.Tail
        dell.Tail = temp
    dell.Size += 1


def push_front(val: Any, dell: DeList) -> None:
    temp: DeNode = DeNode(val)
    if is_empty(dell):
        # filling first node in empty list
        dell.Head = dell.Tail = temp
        dell.Head.Next = dell.Tail
        dell.Tail.Prev = dell.Head
    else:
        # pushing to the right of the list
        temp.Next = dell.Head
        dell.Head.Prev = temp
        dell.Head = temp
    dell.Size += 1 # size up


def pop_back(dell: DeList) -> Any:
    retval: Optional[Any] = None
    if not is_empty(dell):
        retval = dell.Tail.Data
        # re-ref Tail to tail pos-1
        temp = dell.Tail
        dell.Tail = temp.Prev
        # remove ref
        del temp
        dell.Size -= 1
    return retval


def pop_front(dell: DeList) -> Any:
    return object()


if __name__ == '__main__':
    dll = DeList()
    push_back(10, dll)
    push_back(20, dll)
    push_back(30, dll)
    push_back(40, dll)
    print(dll)
    pop_back(dll)
    print(dll)
