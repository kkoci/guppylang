from guppylang import guppy

@guppy.enum
class Enum:
    f = {"m": int}
    Var = {}

@guppy
def main(i: Enum) -> None:
    match i:
        case Enum.f.m():
            pass
        
main.check()
