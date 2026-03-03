@guppy.struct
class MyStruct:
    x: int

@guppy
def foo(s: MyStruct) -> None:
    MyStruct = 42
    match s:
        case MyStruct():
            pass

foo.check()
