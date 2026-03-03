from guppylang import guppy

@guppy.enum
class Enum:
    North = {"A": int}
    South = {"B": int}
    East = {}
    West = {}

@guppy
def main(x: int, a: int) -> None:
    match x:
        case _ if a > 0:
            pass

main.check()
