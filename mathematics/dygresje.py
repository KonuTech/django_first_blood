


def funkcja1(x, **kwargs):
    print("kwargs", kwargs)
    funkcja2(x, **kwargs)

def funkcja2(y, **kwargs):
    print("kwargs z funkcji 2", kwargs)
    if kwargs.get("a"):
        print("Podejmuje dzialanie a")
    
    

def main():
    context = {"a": 1, "b": 2}
    context = dict(a=1, b=2)

    funkcja1(1)
    funkcja1(1, a=1, b=2)
    funkcja1(1, **context)
    funkcja1(1, b=2, c=3)


main()