with open('teksts.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) >= 3:
        print(lines[2])