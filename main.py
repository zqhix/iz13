from functions import find_hole


def main():

    gx, gy = map(float, input().split())
    dx, dy = map(float, input().split())

    n = int(input())

    holes = []

    for _ in range(n):
        hx, hy = map(float, input().split())
        holes.append((hx, hy))

    result = find_hole(
        gx, gy,
        dx, dy,
        holes
    )

    if result == -1:
        print("NO")
    else:
        print(result)


main()
