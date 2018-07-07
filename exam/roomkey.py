def check(rooms):
    a = [False] * (len(rooms))
    b = []
    a[0] = True
    try:
        for x in rooms[0]:
            b.append(x)
            a[x] = True
        while len(b) != 0:
            for x in rooms[b[0]]:
                if x not in b and a[x] is False:
                    b.append(x)
                a[x] = True
            b.remove(b[0])
    except:
        return
    for x in a:
        if x is False:
            print(False)
            break
    else:
        print(True)
check([[1], [0, 2], [3]])
check([[1, 3], [3, 0, 1], [2], [0]])
check([[1, 2, 3], [0], [0], [0]])
check([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
check([[1], [2, 3], [1, 2], [4], [1], [5]])
check([[1], [2], [3], [4], [2]])
check([[1], [1, 3], [2], [2, 4, 6], [], [1, 2, 3], [1]])