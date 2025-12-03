with open("../input.txt") as f:
    banks = f.readlines()

ans = 0
for bank in banks:
    bank = bank.strip('\n')
    sol= [0]
    # iterate over numbers up to the last 12
    for i in range(len(bank) - 12):
        # If we find the largest number is greater than the current, replace and reset list as biggest magnitude is that
        if int(bank[i]) > int(sol[0]) and len(bank) - 1 - i < 12:
            sol = [int(bank[i])]
        else:
            # If the list is less than 12, append an element and check if that element can replace any number in the list
            # If so, replace and truncate to make the last value that element
            if len(sol) < 12:
                sol.append(int(bank[i]))
            for j in range(len(sol)):
                if int(bank[i]) > int(sol[j]):
                    sol[j] = int(bank[i])
                    sol = sol[:j + 1]
                    break
                
    # Iterate of last 12
    for i in range(12, 0, -1):
        # If less than 12 append
        if len(sol) < 12:
                sol.append(int(bank[len(bank) -i]))
        # Then, check the last 12 and only iterate over the sol starting at 12 - i so we have enough numbers. and do the same as above
        for j in range(i):
            if 12 - i + j == len(sol):
                break
            if int(bank[len(bank)- i]) > int(sol[12 - i + j]):
                sol[12 - i + j] = int(bank[len(bank)- i])
                sol = sol[:12 - i + j + 1]
                break

    ans += int("".join(str(x) for x in sol))

print(ans)