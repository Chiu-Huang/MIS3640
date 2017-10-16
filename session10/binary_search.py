def binary_function (x, data):
    data.sort()
    minx = 0
    maxx = len(data)-1
    midx =(minx + maxx)/2
    mid = int (midx)
    iteration = 0
    while data[mid] != x:
        mid = int(midx)
        if data[mid] < x:
            minx = mid + 1
            iteration += 1
        elif data[mid] > x:
            maxx = mid - 1
            iteration += 1
        midx = (maxx+minx)/2
    return mid
print(binary_function(32, [4,8,9,10,24,32,45,56]))
# only works for exact match