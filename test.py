import sys
from typing import Callable

argc = len(sys.argv)
argv = sys.argv

print(f"argc: {argc}")
print(f"argv: {argv}")

print(f"Your age is {argv[1]}")

print(f"argc: {argc}")
print(f"argv: {argv}")

print(f"Your age is {argv[1]}")


def f(a: Callable):
    pass
