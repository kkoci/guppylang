```python
@guppy.enum
class Direction:
    North = {"A": int}
    South = {"B": int}

    @guppy
    def str_(self) -> str:
        return "Direction"

@guppy
def g() -> Direction:
    return Direction.North(5)

@guppy.struct
class Point:
    x: int
    y: int

    @guppy
    def method(self) -> int:
        return self.x + self.y

@guppy
def main(north: Direction, x:int) -> None:
    match north:
        case g():     # match on a function
            x = 99
        case Direction.str_(): # match on a method enun
            x = 88
        case Point.method(): # match on a method struct
            x = 77


main.compile()
```
