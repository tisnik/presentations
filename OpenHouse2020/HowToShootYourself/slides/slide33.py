def createCounter():
    counter = 0

    def next():
        global counter
        counter += 1
        return counter

    return next


def main():
    counter1 = createCounter()
    counter2 = createCounter()
    for i in range(1, 11):
        result1 = counter1()
        result2 = counter2()
        print("Iteration #%d" % i)
        print("    Counter1: %d" % result1)
        print("    Counter2: %d" % result2)


main()
