from guppylang import guppy

@guppy.enum
class Enum:
    North = {"A": int}


    @guppy
    def str_(self) -> str:
        return "Direction"

@guppy
def main(north: Enum, x: int) -> None:
    match p:
        case Enum.North():
            x = 77

main.check()
