## WORKING FEATURE


### Enum

Only checking
```python


match north:
    case Direction.North(): # THIS
        body1
    case Direction.South:
        body2
    case Direction.North(A=steps):  #TODO var definition
        body2
    case Direction.North(A=steps) if steps > 10:
        body1
    case Direction.South as south: 
        body3
    case Direction.East | Direction.West:
        body4
    case x:     
        body5
    case _:                 # THIS
        body5

```


## TODO TO DISCUSS


Which types are allowed?

How should match work with generics?

Making match work with generics

How do we treat `as` statements with linear variables?


## DONE CHECKs

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
    p = Point(3, 4)
    match north:
        case g():  # ERROR: match on a function
            x = 99
        case Direction.str_(): # ERROR: match on a method enum
            x = 88
        case p.method(): # ERROR: match on a struct method
            x = 77
        case x: # ERROR: match-as not supported
            x = 66
        case Class() as var: # ERROR: match-as not supported
            x = 55


@guppy
def main(north: Enum[int], x:int) -> None:
    match north:
        case Point(): # ERROR: different type
            z = 66

```

## TODO CHECKs 


### Unreachable patterns
What do we do for unreachable patterns?
In Python, from this:

```python

 match i:
    case 0:
        return "Zero"
    case 1:
        return "One"
    case x:
        return f"No match for {x}"
    case 3:
        return "Three"
```

we have:
```
Cell In[10], line 8
    case x:
         ^
SyntaxError: name capture 'x' makes remaining patterns unreachable
```

In Rust, from this:
```rust
match i {
    0 => "Zero",
    1 => "One",
    x => format!("No match for {x}"),
    3 => "Three",
}
```

we have:
```
Standard Error
    Compiling playground v0.0.1 (/playground)
warning: unreachable pattern
 --> src/main.rs:7:9
  |
6 |         x => format!("No match for {x}"),
  |         - matches any value
7 |         3 => "Three".to_string(),
  |         ^ no value can reach this
```


### ...

and other stuff