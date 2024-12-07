import copy
from tqdm import tqdm

def read_data():
    with open('Day6/data.txt') as f:
        lines = f.readlines()

    x,y = 0, 0 
    for i, line in enumerate(lines):
        l = []
        for j, char in enumerate(line.strip()):
            if char == "^":
                x,y = i,j
            l.append(char)
            
            lines[i] = l

    return lines, x, y

def move(lines, x, y):
    # directions (counterclockwise):
    # 0 -> Up
    # 1 -> Right
    # 2 -> Down
    # 3 -> Left
    current_direction = 0
    count = 1 # count the initial position
    lines[x][y] = "X" # mark as visited

    while True:
        if current_direction == 0:
            tx, ty = x-1, y
        elif current_direction == 1:
            tx, ty = x, y+1
        elif current_direction == 2:
            tx, ty = x+1, y
        elif current_direction == 3:
            tx, ty = x, y-1

        if tx < 0 or tx >= len(lines) or ty < 0 or ty >= len(lines[0]):
            return count
        
        elif lines[tx][ty] == "#":
            current_direction += 1
            current_direction %= 4
            continue

        else:
            if lines[tx][ty] == ".":
                count += 1
            lines[tx][ty] = "X"
            x,y = tx, ty

def place_obstalce(lines, xi, yi):
    # a slow O(n²) algorithm that brute searches all possible places for placing an obstacle
    count = 0

    backup = copy.deepcopy(lines)
    for i in tqdm(range(len(lines))):
        for j in tqdm(range(len(lines[0]))):
            current_direction = 0
            x, y = xi, yi
            lines[x][y] = '1' # mark as visited
            lines[i][j] = "O"


            while True:
                if current_direction == 0:
                    tx, ty = x-1, y
                elif current_direction == 1:
                    tx, ty = x, y+1
                elif current_direction == 2:
                    tx, ty = x+1, y
                elif current_direction == 3:
                    tx, ty = x, y-1

                if tx < 0 or tx >= len(lines) or ty < 0 or ty >= len(lines[0]):
                    break
                
                elif lines[tx][ty] == "#" or lines[tx][ty] == "O":
                    current_direction += 1
                    current_direction %= 4

                else:
                    if lines[tx][ty] == ".":
                        lines[tx][ty] = "1"
                    else:
                        lines[tx][ty] = f"{int(lines[tx][ty]) + 1}"
                    
                    if int(lines[tx][ty]) >= 3 and int(lines[x][y]) >= 3: #it is arbitarily decided that a loop is done, if both present and next position have been passed at least thrice
                        count += 1
                        break

                    x,y = tx, ty
            lines = copy.deepcopy(backup)

    return count




if __name__ == "__main__":
    lines, x, y = read_data()
    print(move(copy.deepcopy(lines), x, y))
    print(place_obstalce(copy.deepcopy(lines), x, y))