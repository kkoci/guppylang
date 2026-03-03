from guppylang import guppy
from typing import Generic

T = guppy.type_var("T")

@guppy.enum
class Enum(Generic[T]):
    North = {"A": T}

@guppy.struct
class Point(Generic[T]):
    x: T
    y: int

@guppy
def main() -> None:
    match Point(Enum.North(3), 5):
        case Point(Enum.North("7"), _):
            pass

main.check()
