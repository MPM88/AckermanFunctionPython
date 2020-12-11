def AckermanFunction(Number1, Number2):
    if Number1 == 0:
        return Number2 + 1
    else:
        if Number2 == 0:
            return (AckermanFunction(Number1 - 1, 1))
        return (AckermanFunction(Number1 - 1, AckermanFunction(Number1, Number2 - 1)))

if __name__ == "__main__":
    import sys
    try:
        for i in range(4):
            for j in range(5):
                print(AckermanFunction(i, j),end='  ')
            print()
    except RecursionError:
        print("Error: Se alcanzo el maximo de recursion permitido")