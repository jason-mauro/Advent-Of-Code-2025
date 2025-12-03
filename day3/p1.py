with open("../input.txt") as f:
    banks = f.readlines()

ans = 0
for bank in banks:
    bank = bank.strip('\n')
    first = 0
    second = 0
    # Find the largest number such that it is not the last index and the second largest after the first in the string
    for i in range(len(bank)):
        if int(bank[i]) > int(first) and not i == len(bank) - 1:
            first = bank[i]
            second = bank[i + 1]
        elif int(bank[i]) > int(second):
            second = bank[i]   
    ans += int(str(first) + str(second))

print(ans)