from guppylang import guppy

@guppy.enum
class Enum:
    North = {"A": int}
    South = {"B": int}
    East = {}
    West = {}

    @guppy
    def str_(self) -> str:
        return "Direction"

@guppy
def main(north: Enum, x: int) -> None:
    match north:
        case p():
            x = 77

main.check()
