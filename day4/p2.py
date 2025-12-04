with open("../input.txt") as f:
    lines = f.read().split('\n')

lines = [list(line) for line in lines]
def in_bounds(x,y):
    return 0 <= x < len(lines[0]) and 0 <= y < len(lines)

dd = [[0, 1], [0, -1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
pos = []
ans = 0
num_removed = -1
while num_removed != 0:
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != "@":
                continue
            count = 0 
            for dx,dy in dd:
                if count > 3: break
                x1 = x + dx
                y1 = y + dy
                if in_bounds(x1,y1) and lines[y1][x1] == '@':
                    count += 1
            if count < 4: 
                pos.append([x,y])
                ans += 1
    num_removed = len(pos)
    for x,y in pos:
        lines[y][x] = '.'      
    pos = []    

# Debug function
# for y in range(len(lines)):
#     for x in range(len(lines[0])):
#         if [x,y] in pos:
#             print('x', end="")
#         else:
#             print(lines[y][x], end="")
#     print("")

print(ans)