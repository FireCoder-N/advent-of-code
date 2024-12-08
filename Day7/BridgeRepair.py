from itertools import product
from tqdm import tqdm

def read_data():
    with open('Day7/data.txt') as f:
        lines = f.readlines()

    return lines


def part1(lines):
    # Reference: https://stackoverflow.com/questions/45990454/generating-all-possible-combinations-of-characters-in-a-string

    count = 0
    operators = ["*", "+"]

    for line in lines:
        l = line.strip().split(": ")
        result = int(l[0])
        operands = l[1:][0]
        combs = ["".join(comb) for comb in product(operators, repeat=(len(operands.split())-1))]

        for comb in combs:
            operands = l[1:][0].split()

            for i, op in enumerate(comb):
                operands.insert(2*i+1, op)

            while len(operands) > 1:
                operands = [str(eval("".join(operands[:3])))] + operands[3:]

            if int(operands[0]) == result:
                count += result
                break

    return count

def part2(lines):
    count = 0
    operators = ["*", "+", "|"] #|| was replaced with | as it is easier to del with


    for line in tqdm(lines):
        l = line.strip().split(": ")
        result = int(l[0])
        operands = l[1:][0]
        combs = ["".join(comb) for comb in product(operators, repeat=(len(operands.split())-1))]

        for comb in combs:
            operands = l[1:][0].split()

            for i, op in enumerate(comb):
                    operands.insert(2*i+1, op)

            while len(operands) > 1:
                t = "".join(operands[:3])
                t = t.replace("|", "")
                operands = [str(eval(t))] + operands[3:]

            if int(operands[0]) == result:
                count += result
                break

    return count


if __name__ == "__main__":
    lines = read_data()
    # print(part1(lines))
    print(part2(lines))