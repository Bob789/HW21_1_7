#fbinachi
def fib(index: int)-> int:
    if index < 1:
        return 0
    if index == 1:
        return 1
    a = 1
    b = 1
    c = None
    for i in range(2, index):
        c = a + b
        a = b
        b = c
    return c

index = 6
print(f" element in in place {index} is: {fib(index)}")

    #  1 2 3 4 5 6 7  8
    #  1 1 2 3 5 8 13 21
