from guppylang import guppy
from guppylang.std.quantum import qubit
from tests.util import compile_guppy

@guppy.struct
class Point:
    x: int
    y: int

@compile_guppy
def main(p: Point) -> int:
    match p:
        case Point(3, _):
            q = qubit()  # ERROR: q created but not consumed before arm ends
            result = 1
        case Point(_, 4):
            result = 2
        case _:
            result = 0
    
    return result
