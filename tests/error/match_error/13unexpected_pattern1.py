from guppylang import guppy
from guppylang.std.quantum import qubit
import guppylang

guppylang.enable_experimental_features()

@guppy.enum
class Enum:
    North = {"q": int}

@guppy
def f(e: Enum) -> None:
    match e:
        case Enum.North:
            pass

f.check()
