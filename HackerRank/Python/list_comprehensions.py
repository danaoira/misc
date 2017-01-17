if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    L = []

    for a in range(0, x + 1):
        for b in range(0, y + 1):
            for c in range(0, z + 1):
                if a + b + c is not n:
                    L.append([a, b, c])
    print(L)