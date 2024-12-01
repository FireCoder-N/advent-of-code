def read_data():
    L1 = []
    L2 = []

    with open('Day1/data.txt') as f:
        numbers = f.readlines()

        for line in numbers:
            l1, l2 = line.split()

            L1.append(int(l1))
            L2.append(int(l2))

    if len(L1) != len(L2):
        print("The lists are not of the same length")
        exit()

    return L1, L2

def total_distance(L1, L2):
    csum = 0

    L1 = sorted(L1)
    L2 = sorted(L2)

    for i in range(len(L1)):
        csum += abs(L1[i] - L2[i])

    return csum

def similarity_score(L1, L2):
    score = 0

    for i in L1:
        score += i * L2.count(i)

    return score




######################################################
if __name__ == '__main__':
    L1, L2 = read_data()
    print(total_distance(L1, L2))
    print(similarity_score(L1, L2))
