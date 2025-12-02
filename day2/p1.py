with open("../input.txt") as f:
    line = f.read().split(",")


ans = 0
for r in line:
    nums = r.split("-")
    start =  int(nums[0])
    end = int(nums[1])
    for j in range(start, end + 1):
        num = str(j)
        if (len(num) % 2 == 0):
            if num[:len(num)//2] == num[len(num)//2:]:
                ans += j
print(ans)