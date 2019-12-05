def morris(n):
    c = "1"
    i = 1
    yield c
    while i <= n:
        current = None
        acc, curr = [], []
        for x in range(len(c)):
            char = c[x]
            if current is None or current != char:
                current = char
                curr = [char, 1]
                acc.append(curr)
            else:
                curr[1] = curr[1] + 1
        c = "".join([str(x[1]) + str(x[0]) for x in acc])
        yield c
        i = i + 1


for x in morris(30):
    print(len(x))

# 5808
