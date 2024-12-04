import re

def read_data():
    with open('Day3/data.txt') as f:
        return "".join(f.readlines())
    

def part1(data):
    # mul(X,Y)
    regex = "mul\(\d{1,3},\d{1,3}\)" # https://regexr.com/
    total = 0

    mul_commands = re.findall(regex, data)

    for i in mul_commands:
        n1, n2 = i[4:-1].split(",") # exclude mul( )
        total += int(n1) * int(n2)

    return total


def part2(data):
    # Inspired by https://github.com/mebeim/aoc/blob/master/2024/README.md#day-3---mull-it-over
    enabled = True
    total = 0
    regex = "(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"

    for mul, do, dont in re.findall(regex, data):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            n1, n2 = mul[4:-1].split(",")
            total += int(n1) * int(n2)

    return total


if __name__ == "__main__":
    part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    data = read_data()
    print(part1(data))
    print(part2(data))