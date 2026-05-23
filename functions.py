import math


def distance_points(x1, y1, x2, y2):
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )


def find_hole(gx, gy, dx, dy, holes):
    for index, hole in enumerate(holes, start=1):

        hx = hole[0]
        hy = hole[1]

        gopher_distance = distance_points(
            gx, gy,
            hx, hy
        )

        dog_distance = distance_points(
            dx, dy,
            hx, hy
        )

        if dog_distance >= 2 * gopher_distance:
            return index

    return -1
