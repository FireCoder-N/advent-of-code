from tqdm import tqdm

def read_data():
    with open('Day11/data.txt') as f:
        lines = f.readlines()

    return [int(l) for l in lines[0].strip().split()]

def blink(line):
    skip = False

    for i, num in enumerate(line):

        if skip:
            skip = not skip
            continue

        x = line.pop(i)

        if x == 0:
            x = 1
            line.insert(i, x)
            continue

        xstr = str(x)
        xlen = len(xstr)
        if xlen%2 == 0:
            x1 = xstr[:xlen//2]
            x2 = xstr[xlen//2:]
            line.insert(i,int(x1))
            line.insert(i+1,int(x2))
            skip = True
            continue

        line.insert(i,x*2024)

    return line


if __name__ == "__main__":
    line = read_data()

    for _ in tqdm(range(25)):
        line = blink(line)
    print(len(line))