with open("../input.txt") as f:
    lines = f.readlines()

start  = lines[0].find("S")

# (line, index) = number of timelines created on a given path starting point
visited = dict()

def dfs_left(line, index, timelines):
    start = index
    for i in range(line, len(lines) - 1):
        if lines[i][index] == "^":
            # Add number of timelines in the right
            if (i, index + 1) in visited:
                timelines += visited[(i, index + 1)]
            else:
                timelines += dfs_right(i, index + 1, 1)
            index = index - 1 # Go left
    # Cache result for staring point
    visited[(line, start)] = timelines
    return timelines

def dfs_right(line, index, timelines):
    start = index
    for i in range(line, len(lines) - 1):
        if lines[i][index] == "^":
            # Add number of timelines in the left timeline
            if (i, index -1) in visited:
                timelines += visited[(i, index -1)]
            else:
                timelines += dfs_left(i, index - 1, 1)
            index = index + 1 # Go right
    # Cache timelines for starting point
    visited[(line, start)] = timelines
    return timelines

print(dfs_right(0, start, 1))

    

    
