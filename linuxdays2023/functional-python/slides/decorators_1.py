#
# Vytvoření a aplikace nového dekorátoru
#

from funcy import decorator


@decorator
def wrapper1(function):
    print("-" * 40)
    function()
    print("-" * 40)


@wrapper1
def hello():
    print("Hello!")


hello()
