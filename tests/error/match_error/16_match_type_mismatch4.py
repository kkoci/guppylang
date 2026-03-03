from typing import Generic

from guppylang import guppy
import guppylang

guppylang.enable_experimental_features()

T = guppy.type_var("T")
x = "1"
@guppy.enum
class Enum(Generic[T]):              # pyright: ignore[reportInvalidTypeForm]
    Var = {"value": T}                      # pyright: ignore[reportInvalidTypeForm]

@guppy
def main(d: Enum[T]) -> None:         # pyright: ignore[reportInvalidTypeForm]
    match d:
        case Enum.Var(1):
            pass

main.compile().modules[0].render_dot()
