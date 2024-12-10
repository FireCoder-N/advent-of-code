def read_data():
    with open('Day8/data.txt') as f:
        lines = f.readlines()

    return lines

def locate_antennas(lines):
    antennas = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != ".":
                if char not in antennas.keys():
                    antennas[char] = []
                antennas[char].append((x,y))

    return antennas

def find_equation(x1, y1, x2, y2):
    if y1 == y2:
        return f"y=={y1}"
    elif x1 == x2:
        return f"x=={x1}"
    else:
        # generalized equation, so that division with (x2-x1) is avoided
        return f"(y-{y2})*{x2-x1}=={y2-y1}*(x-{x2})"
    
def distance(x1, y1, x2, y2):
    # manhattan distance, so that we don't have to deal with decimals (and/or irrational numbers)
    return abs(y2-y1) + abs(x2-x1)

def part1(antennas, maxx, maxy):
    antinodes = []

    for key in antennas.keys():
        locations = antennas[key]

        for i in locations:
            for j in locations:
                if i == j:
                    continue
                eq = find_equation(i[0], i[1], j[0], j[1])
                for y in range(maxy):
                    for x in range(maxx):
                        if eval(eq) and (distance(x,y,i[0], i[1]) == 2*distance(x,y,j[0], j[1]) or 2*distance(x,y,i[0], i[1]) == distance(x,y,j[0], j[1]) ):
                            if (x,y) not in antinodes:
                                antinodes.append((x,y))
    
    return len(antinodes)

def part2(antennas, maxx, maxy):
    # by using the brute force method presented above for part 1, part 2 is actually easier,
    # since it has less constraints (i.e. the distance clause is elimminated). LoL :)
    antinodes = []

    for key in antennas.keys():
        locations = antennas[key]

        for i in locations:
            for j in locations:
                if i == j:
                    continue
                eq = find_equation(i[0], i[1], j[0], j[1])
                for y in range(maxy):
                    for x in range(maxx):
                        if eval(eq) and (x,y) not in antinodes:
                                antinodes.append((x,y))
    
    return len(antinodes)


#################################
if __name__ == "__main__":
    lines = read_data()
    antennas = locate_antennas(lines)
    print(part1(antennas, len(lines[0].strip()), len(lines)))
    print(part2(antennas, len(lines[0].strip()), len(lines)))