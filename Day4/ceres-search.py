
def read_data():
    with open('Day4/data.txt') as f:
        lines = f.readlines()

    # new_lines = []
    # for line in lines:
    #     new_lines.append([l for l in line])

    return lines


def horizontal_search(lines):
    count = 0

    for l in lines:
        for i in range(len(l)-3):
            if l[i:i+4] == "XMAS" or l[i:i+4] == "SAMX":
                count += 1

    return count


def vertical_search(lines):
    count = 0

    for i in range(len(lines[0].strip())):
        column = "".join([l[i] for l in lines])
        for j in range(len(column)-3):
            if column[j:j+4] == "XMAS" or column[j:j+4] == "SAMX":
                count += 1

    return count

def diagonal_search(lines):
    count = 0 

    for l in range(len(lines)-3):
        for c in range(len(lines[0].strip())-3):
            primary = lines[l][c] + lines[l+1][c+1] +  lines[l+2][c+2] + lines[l+3][c+3]
            secondary = lines[l][c+3] + lines[l+1][c+2] + lines[l+2][c+1] + lines[l+3][c]
            if primary == "XMAS" or primary == "SAMX":
                count += 1

            if secondary == "XMAS" or secondary == "SAMX":
                count += 1

    return count

def mas_search(lines):
    count = 0 

    for l in range(len(lines)-2):
        for c in range(len(lines[0].strip())-2):
            primary = lines[l][c] + lines[l+1][c+1] +  lines[l+2][c+2]
            secondary = lines[l][c+2] + lines[l+1][c+1] + lines[l+2][c]
            if (primary == "MAS" or primary == "SAM") and (secondary == "MAS" or secondary == "SAM") :
                count += 1

    return count


##################################################
if __name__ == "__main__":
    lines = read_data()
    total1 = horizontal_search(lines) + vertical_search(lines) + diagonal_search(lines)
    print(total1)

    total2 = mas_search(lines)
    print(total2)