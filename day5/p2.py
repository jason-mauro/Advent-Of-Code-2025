with open('../input.txt') as f:
    parts = f.read().split('\n\n')


db = parts[0].split('\n')

count = 0
ranges = []
for row in db:
    p = row.split("-")
    q = [[int(p[0]),int(p[1])]]
    # NOTE: Ranges are inlcusive
    # Go until no sub-ranges left
    while q:
        start, end = q.pop()
        length = len(q)
        addVals = True
        for r in ranges:
            s, e = r
            # we enclose a range then search the non-inclusive sub-ranges
            if start <= s <= e <= end:
                q.append([start,s - 1])
                q.append([e + 1,end])
                addVals = False
                break
            elif s <= start <= end <= e: # Then enclose our range so ignore this range
                addVals = False
                break
            elif s <= start <= e <= end: # search from e + 1 to end as new range
                start = e + 1
            elif start <= s <= end <= e: # search from start to s - 1 as new range
                end = s - 1

        if  addVals: # Add the subrange (inclusive)
            count += end - start + 1
    
    # Append the range
    ranges.append([int(p[0]),int(p[1])])

print(count)