from guppylang import guppy
from guppylang.std.quantum import qubit
from tests.util import compile_guppy

@guppy.struct
class Point:
    x: qubit
    y: int

@guppy
def fun() -> Point:
    return Point(qubit(), 4)

@guppy
def describe_point(point: Point)-> Point:
    return Point(qubit(), 3)

@compile_guppy
def main() -> None:
    match describe_point(fun()):
        case _:
            pass

