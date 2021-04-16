"""
@author: Daniel Herrera-Vazquez
"""
from dataclasses import dataclass
from typing import Any, Optional, NewType, Generic, TypeVar
from infix import or_infix


DeNode: type = NewType('DeNode', object)
DeList: type = NewType('DeList', object)
T = TypeVar('T')


@dataclass
class DeNode(Generic[T]):
    Next: Optional[DeNode] = None
    Prev: Optional[DeNode] = None
    Data: Optional[T] = None


@dataclass
class DeList(Generic[T]):
    Head: Optional[DeNode] = None
    Tail: Optional[DeNode] = None
    Size: int = 0


def is_empty(dell: DeList) -> bool:
    return dell.Size == 0


@or_infix
def push_back(dell: DeList, val: T) -> None:
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


@or_infix
def push_front(dell: DeList, val: T) -> None:
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


def pop_back(dell: DeList) -> T:
    retval: Optional[T] = None
    if not is_empty(dell):
        retval = dell.Tail.Data
        # re-ref Tail to tail pos-1
        temp = dell.Tail
        dell.Tail = temp.Prev
        # remove ref
        del temp
        dell.Size -= 1
    return retval


def pop_front(dell: DeList) -> T:
    return object()


if __name__ == '__main__':
    dll = DeList[int]()
    # container on lval, data on rval
    dll |push_back| 10
    dll |push_back| 20
    dll |push_back| 30
    dll |push_back| 40
    print(dll)
    pop_back(dll)
    print(dll)
