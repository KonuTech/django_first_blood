def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def div(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Arg b cannot be 0 because we cannot divide by 0")
    return a / b

def mul(a: int, b: int) -> int:
    return a * b


operations = {
    "add": add,
    "sub": sub,
    "div": div,
    "mul": mul
}

# f = add

# f(1, 2)

class AlgebraService:

    @staticmethod
    def calculate(operation: str, a:int, b:int) -> int | float:

        # func = operations[operation]
        # func(a, b)
        return operations[operation](a, b)

