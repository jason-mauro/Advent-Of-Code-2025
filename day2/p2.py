with open("../input.txt") as f:
    line = f.read().split(",")

ans = 0
for r in line:
    nums = r.split("-")
    start =  int(nums[0])
    end = int(nums[1])
    for j in range(start, end + 1):
        if j < 10: 
            continue
        num = str(j)
        # Iterate through half the string and check if [:i] substring elminates the whole string and thus is repeating
        # better way is probably iterating and checkign if a chunk size would be valid then checking for sequential substring but python is easy
        for l in range(1, len(num) // 2 + 1):
            if len(list(filter(None, list(num.split(num[:l]))))) == 0:
                ans += j
                break

print(ans)