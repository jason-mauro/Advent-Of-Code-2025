with open("input.txt") as f: 
    lines = f.splitLines()
diff = 0
start = 50
last = 50
password = 0

for line in lines:
    match line[0]:
        case 'R':
            diff = int(line[1:])
            # Get number of rotations
            if diff >= 100:
                password += diff // 100
            diff = diff % 100
            # If greater than 0 we went over 0
            if start + diff > 100:
                password += 1
            # Get new value
            start = (start + diff) % 100
        case 'L':
            # Get diff, number of rotations and the actual diff % 100
            diff = int(line[1:])
            if diff >= 100:
                password += diff // 100
                diff = diff % 100
            # Turn left
            start = start - diff
            # If negative we subtract from 100
            if start < 0:
                start = 100 + start
                # dont double count if at 0 already and going left
                if last != 0:
                    password += 1
    # If the last was 0 and we went back, dont double count
    if last != 0 and start == 0:
        password += 1
    last = start


print (password)