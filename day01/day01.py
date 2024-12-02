def part1(left, right):
    left, right = sorted(left), sorted(right)
    total = sum([abs(r-l) for l, r in zip(left, right)])
    print("part1: ", total)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]

    left, right = [], []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    part1(left, right)

