from guppylang import guppy
from guppylang.std.quantum import qubit, owned
from tests.util import compile_guppy

@guppy.enum
class LinearEnum:
    var = {"a": qubit}


@compile_guppy
def main(e: LinearEnum @owned) -> None: # pyright: ignore[reportInvalidTypeForm]
    match e:
        case LinearEnum.var(_):
            pass

