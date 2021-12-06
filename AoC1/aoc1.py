import sys

x = None
counter = 0

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines:
        if x < line:
            counter += 1
        x = line
print(counter)
