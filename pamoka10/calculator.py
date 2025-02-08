print(f"I AM IN CALCULATOR>PY __name__ is{__name__}")

def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def prod(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> int:
    return x // y

if __name__ == "__main__":
    addition = add(5, 5)
    print(addition)