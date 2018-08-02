ages = [10, 16, 43, 22, 67, 59]

min = ages[0]
max = ages[0]

for x in ages:
    if (x < min):
        min = x

    if (x > max):
        max = x

print(max-min)
