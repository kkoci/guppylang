from guppylang import guppy

@guppy.enum
class Enum:
    North = {"A": int}
    South = {"B": int}
    East = {}
    West = {}

    @guppy
    def method(self) -> str:
        return "Direction"

@guppy
def main(north: Enum, x: int) -> None:
    match north:
        case north.method():
            x = 77

main.check()
