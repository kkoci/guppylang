from guppylang import guppy

@guppy.struct
class Point:
    x: int
    y: int

@guppy
def main(p: Point, x: int) -> None:
    match p:
        case Point():
            z = 66

main.check()

#TODO: NICOLA do the same for enums