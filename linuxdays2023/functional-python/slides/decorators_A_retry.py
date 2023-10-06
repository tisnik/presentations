#
# Dekorátor @retry
#

from funcy import retry


@retry(4, timeout=lambda delay: 2 ** delay, errors=Exception)
def call_function_to_raise_exception():
    print("Trying to call problematic code...")
    raise_exception()


def raise_exception():
    raise Exception("foo")


while True:
    call_function_to_raise_exception()
