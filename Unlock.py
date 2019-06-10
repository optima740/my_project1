def PatternUnlock(N, hits):
    if N != len(hits):
        return
    graph = []
    a = {6:1, 9:1, 2:1, 8:1.41421, 5:2}
    b = {1:1, 3:1, 8:1, 5:1, 9:1.41421, 6:1.41421, 4:1.41421, 7:1.41421}
    c = {2:1, 4:1, 7:1, 8:1.41421, 5:1.41421}
    d = {3:1, 5:1, 2:1.41421}
    e = {4:1, 2:1, 6:1, 3:1.41421, 1:1.41421}
    f = {5:1, 1:1, 2:1.41421}
    g = {2:1.41, 3:1, 8:1}
    h = {7:1, 2:1, 9:1, 3:1.41421, 1:1.41421}
    i = {8:1, 1:1, 2:1.41421}

    graph.append(a)
    graph.append(b)
    graph.append(c)
    graph.append(d)
    graph.append(e)
    graph.append(f)
    graph.append(g)
    graph.append(h)
    graph.append(i)

    s = 0
    for x in range (N-1):
        s += graph[(hits[x])-1][hits[x+1]]

    s1 = round(s, 5)

    st = str(s1)
    st = st.replace("0", "")
    st = st.replace(".", "")

    return st


