with open("../input.txt") as f:
    lines = f.readlines()

lines = [l.replace("\n", "") for l in lines]

ans = 0
i = 0
while i < len(lines[0]):
    start = i
    op = lines[len(lines) - 1][i]

    j = i + 1
    # Get the range of columns to search for this number
    while 0 <= j < len(lines[0]) and lines[len(lines) - 1][j] == ' ' :
        j += 1

    nums = ["" for i in range(j - i)]

    # for each column to search iterate the rows and if number add it to the its repective index in nums
    for z in range(j - i):
        for lineIndex in range(len(lines)- 1):
            if lines[lineIndex][start + z] != " ":
                nums[z] += lines[lineIndex][start + z]
    # remove empty columns
    nums = list(filter(lambda num: num != '', nums))

    # Sum or multiply the values
    count = int(nums[0])
    if op == '*':
        for k in range(1, len(nums)):
            if nums[k] != " ":
                count *= int(nums[k])
    else:
        for k in range(1, len(nums)):
            if nums[k] != " ":
                count += int(nums[k])
    ans += count
    # Go to next op
    i = j    

print(ans)
        
        
