def read_data():
    with open('Day12/data.txt') as f:
        lines = f.readlines()

    return [[l for l in line.strip()] for line in lines]

def part1(lines):
    global area, perimeter

    visited = [[False for _ in row] for row in lines]
    total = 0 
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):

            if visited[i][j]:
                continue

            area = 0
            perimeter = 0

            flood_fill(lines, char, i, j, visited)
            total += area*perimeter

    return total



def flood_fill(lines, target, i, j, visited):
    global area, perimeter

    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i][j] != target:
        return True
    elif visited[i][j]:
        return False

    visited[i][j] = True
    area += 1

    south_not_found = flood_fill(lines, target, i+1, j, visited)  # S
    if south_not_found:
        perimeter += 1

    north_not_found = flood_fill(lines, target, i-1, j, visited)  # N
    if north_not_found:
        perimeter += 1

    east_not_found = flood_fill(lines, target, i, j+1, visited)  # E
    if east_not_found:
        perimeter += 1

    west_not_found = flood_fill(lines, target, i, j-1, visited)  # W
    if west_not_found:
        perimeter += 1

    return

if __name__ == "__main__":
    area = 0
    perimeter = 0
    # lines = [["A", "A", "A", "A"], ["B", "B", "C", "D"], ["B", "B", "C", "C"], ["E", "E", "E", "C"]]
    # flood_fill(lines, "C", 1, 2, [[False for _ in row] for row in lines])
    # pass
    lines = read_data()
    print(part1(lines))