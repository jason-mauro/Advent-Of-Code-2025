with open('../input.txt') as f:
    parts = f.read().split('\n\n')


db = parts[0].split('\n')

ranges = []
# parse ranges
for row in db:
    p = row.split("-")
    ranges.append([int(p[0]), int(p[1])])

ingredients = parts[1].split("\n")
count = 0
# Check if in any of the ranges and add to count
for i in ingredients:
    for r in ranges:
        if r[0] <= int(i) <= r[1]:
            count += 1
            break
print(count)