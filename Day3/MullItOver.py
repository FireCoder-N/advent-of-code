import re

def read_data():
    with open('Day3/data.txt') as f:
        return f.readlines()
    
def part1(lines):
    # mul(X,Y)
    regex = "mul\(\d{1,3},\d{1,3}\)" # https://regexr.com/
    total = 0

    for l in lines:
        mul_commands = re.findall(regex, l)

        for i in mul_commands:
            n1, n2 = i[4:-1].split(",") # exclude mul( )
            total += int(n1) * int(n2)

    return total


if __name__ == "__main__":
    data = read_data()
    total = part1(data)
    print(total)