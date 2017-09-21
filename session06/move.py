def move(n, source, bridge, destination):
    if n > 1:
        move (n-1, source, destination, bridge)
        move (1, source, bridge, destination)
        move (n-1, bridge, source, destination)
    if n == 1:
        print (source, " -> ", destination)


move (3, "A", "B", "C")