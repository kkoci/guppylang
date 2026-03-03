from guppylang import guppy

@guppy.enum
class Enum:
    North = {"A": int}

@guppy.struct
class Point:
    x: int

@guppy
def main(north: Enum) -> None:
    match north:
        case Point(1):
            pass

main.check()

# TODO: NICOLA do the same for enums