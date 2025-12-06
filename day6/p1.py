with open("../input.txt") as f:
    lines = f.readlines()

nums = [l.split() for l in lines]

ans = 0
for i in range(len(nums[0])):
    count = int(nums[0][i])
    if nums[len(lines) - 1][i] == '+':
        for j in range(1, len(lines)- 1):
            count += int(nums[j][i])
    elif nums[len(lines) - 1][i] == '*':
        for j in range(1, len(lines)- 1):
            count *= int(nums[j][i])
    ans += count
print(ans)
        
        
