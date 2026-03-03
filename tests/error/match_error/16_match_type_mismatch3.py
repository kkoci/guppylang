from typing import Generic

from guppylang import guppy
import guppylang

guppylang.enable_experimental_features()

T = guppy.type_var("T")

@guppy.struct
class Point(Generic[T]):
    A: T

@guppy
def main(d: Point[T]) -> None:
    match d:
        case Point(1):
            pass

main.compile().modules[0].render_dot()
