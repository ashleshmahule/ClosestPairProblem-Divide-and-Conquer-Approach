import math


def find_distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + (math.pow(p1[1] - p2[1], 2)))


def brute_force(p, n):
    min = float(99999)
    for i in range(0, int(n)):
        for j in range(i + 1, int(n)):
            if find_distance(p[i], p[j]) < min:
                min = find_distance(p[i], p[j])
    return min


def strip_closest(strip, size, dist):
    min = dist

    for i in range(0, size):
        for j in range(i + 1, size):
            if find_distance(strip[i], strip[j]) < min:
                min = find_distance(strip[i], strip[j])
    return min


def find_closest(px, py, n):
    if n <= 3:
        return brute_force(px, n)

    mid = n / 2
    midpoint = px[int(mid)]

    pyl = []
    pyr = []

    for i in range(len(py)):
        if py[i][0] <= midpoint[0]:
            pyl.append(py[i])
        else:
            pyr.append(py[i])

    dl = find_closest(px, pyl, int(mid))
    dr = find_closest(px, pyr, int(n) - int(mid))

    d = min(dl, dr)

    strip = []
    j = int(0)

    for i in range(len(py)):
        if abs(py[i][0] - midpoint[0]) < d:
            strip.append(py[i])
            j += 1

    return min(d, strip_closest(strip, j, d))


def closest_points(p, n):
    px = []
    py = []

    for i in range(0, n):
        px.append(p[i])
        py.append(p[i])

    px = sorted(px, key=lambda x: (x[0], x[1]))
    py = sorted(py, key=lambda x: (x[1], x[0]))

    print('Sorted acc to x')
    print(px)
    print('Sorted acc to y')
    print(py)

    return find_closest(px, py, n)


if __name__ == '__main__':
    points = [[12, 10], [3, 4], [1, 2], [6, 7], [2, 1], [3, 2], [4, 5], [8, 9], [4, 0], [1, 10],[2,10]]
    print(closest_points(points, int(len(points))))
