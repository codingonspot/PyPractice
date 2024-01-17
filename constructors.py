class A:
    attr1 = "sample"

    def __init__(self, o):
        self.o = o


if __name__ == '__main__':
    ob1 = A("Object 1")
    ob2 = A("Object 2")
    x = ob1.__class__.attr1
    print(f"Objec1 is a {x}")
