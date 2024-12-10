def read_data():
    with open('Day9/data.txt') as f:
        lines = f.readlines()

    return lines

def expand(inp):
    new = ""
    for i, num in enumerate(inp):
        if i % 2 == 0:
            new += int(num)*f"{i//2}"
        else:
            new += int(num)*"."

    return new

def fragment(inp):
    for i in range(len(inp)):
        if inp[i] == ".":
            for j in range(len(inp)-1,0,-1):
                if j <= i:
                    return inp
                
                if inp[j] != ".":
                    inp = inp[:i] + inp[j] + inp[i+1:j] + inp[i] + inp[j+1:]
                    break

def checksum(inp):
    total = 0
    for i, num in enumerate(inp):
        total += int(num)*i
    return total

if __name__ == "__main__":
    inp = read_data()[0].strip()
    total = fragment(expand(inp))
    print(total)