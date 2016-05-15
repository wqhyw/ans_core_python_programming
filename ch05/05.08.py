#! /usr/bin/env python

def square(edge):
    return edge * edge


def cube(edge):
    return edge * edge * edge


def circle(radius):
    return radius * radius * 3.14159265


def ball(radius):
    return (radius ** 3) * 3.14159265 * 4 / 3


def test():
    print square(1.2)
    print cube(1.2)
    print circle(1.2)
    print ball(1.2)


if __name__ == "__main__":
    test()
