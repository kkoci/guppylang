from guppylang import guppy

@guppy.enum
class Enum:
    North = {}
    South = {}
    East = {}
    West = {}

@guppy
def main(x: int, a: int) -> None:
    match x:
        case Enum.North() | Enum.South():
            pass

main.check()
