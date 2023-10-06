#
# Dekorátor @retry
#

from funcy import retry


@retry(3, timeout=1)
def call_function_to_raise_exception():
    print("Trying to call problematic code...")
    raise_exception()


def raise_exception():
    raise Exception("foo")


while True:
    call_function_to_raise_exception()
