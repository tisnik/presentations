#
# Vytvoření a aplikace nového dekorátoru
#

from funcy import decorator


@decorator
def wrapper1(function):
    print("-" * 40)
    function()
    print("-" * 40)


@decorator
def wrapper2(function):
    print("=" * 40)
    function()
    print("=" * 40)


@wrapper1
@wrapper2
def hello():
    print("Hello!")


hello()
