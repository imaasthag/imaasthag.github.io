part1 = 1
part2 = 1
current = 2

while (current < 10000):
    print(current)
    part1 = part2
    part2 = current
    current = part1 + part2
