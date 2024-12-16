def read_data():
    with open('Day10/data.txt') as f:
        lines = f.readlines()

    return [[int(l) for l in line.strip()] for line in lines]

def find_num(searchnum, lines):
    positions = []

    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            if num == searchnum:
                positions.append((i,j))

    return positions

########
# Part 1
# ###### 

def find_paths_score(lines):
    global score

    total_score = 0

    for i, j in find_num(0, lines):
        score = 0
        visited = [[False for _ in row] for row in lines]
        flood_fill_score(lines, 0, i, j, visited)
        total_score += score

    return total_score
            

def flood_fill_score(lines, target, i, j, visited):
    global score

    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i][j] != target or visited[i][j]:
        return
    
    visited[i][j] = True

    if lines[i][j] == 9:
        score += 1
        return

    flood_fill_score(lines, target+1, i+1, j, visited)  # S
    flood_fill_score(lines, target+1, i-1, j, visited)  # N
    flood_fill_score(lines, target+1, i, j+1, visited)  # E
    flood_fill_score(lines, target+1, i, j-1, visited)  # W

    return


########
# Part 2
# ###### 

def find_paths_rating(lines):
    global rating

    total_rating = 0

    for i, j in find_num(0, lines):
        rating = 0
        flood_fill_rating(lines, 0, i, j)
        total_rating += rating

    return total_rating
            

def flood_fill_rating(lines, target, i, j):
    global rating

    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i][j] != target:
        return

    if lines[i][j] == 9:
        rating += 1
        return

    flood_fill_rating(lines, target+1, i+1, j)  # S
    flood_fill_rating(lines, target+1, i-1, j)  # N
    flood_fill_rating(lines, target+1, i, j+1)  # E
    flood_fill_rating(lines, target+1, i, j-1)  # W

    return

if __name__ == "__main__":
    score = 0
    rating = 0
    lines = read_data()
    print(find_paths_score(lines))
    print(find_paths_rating(lines))