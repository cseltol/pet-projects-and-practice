from typing import *


T = TypeVar("T")

class Factor(NamedTuple, Generic[T]):
    elements: List[int]
    levels: Mapping[T, int]


def factor(xs: List[T]) -> Factor[T]:
    pass

# TypeError: metaclass conflict:
#   the metaclass of a derived class must be
#   a (non-strict) subclass of the metaclasses
#   of all this bases
