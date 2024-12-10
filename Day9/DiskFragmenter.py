def read_data():
    with open('Day9/data.txt') as f:
        lines = f.readlines()

    return lines

def expand(inp):
    new = []
    for i, num in enumerate(inp):
        if i % 2 == 0:
            for _ in range(int(num)):
                new.append(f"{i//2}")
        else:
            for _ in range(int(num)):
                new.append(".")

    return new

def fragment(inp):
    last = len(inp)-1
    for i in range(len(inp)):
        if inp[i] == ".":
            while inp[last] == ".":
                last -= 1

            if last <= i:
                return inp
                
            if inp[last] != ".":
                inp = inp[:i] + [inp[last]] + inp[i+1:last] + [inp[i]] + inp[last+1:]

def checksum(inp):
    total = 0
    for i, num in enumerate(inp):
        if num == ".":
            continue
        total += int(num)*i

    return total

if __name__ == "__main__":
    inp = read_data()[0].strip()
    fr = fragment(expand(inp))
    print(checksum(fr))
