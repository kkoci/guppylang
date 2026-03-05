from guppylang import guppy
from guppylang.std.quantum import qubit
from tests.util import compile_guppy

@guppy.struct
class Point:
    x: qubit
    y: int

@compile_guppy
def main(p: Point) -> None:
    match p:
        case Point(_, _):
            b = p.x
        case Point(_, 1):
            pass
        case _:
            pass

