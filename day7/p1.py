with open("../input.txt") as f:
    lines = f.readlines()

start  = lines[0].find("S")

q = [start]

count = 0
for i in range(1, len(lines) - 1): 
    newq = set()
    for index in q:
        if lines[i][index] == "^":
            count += 1
            newq.add(index - 1)
            newq.add(index + 1)
        else:
            newq.add(index)
    q = list(newq)
print(count)

    

    
