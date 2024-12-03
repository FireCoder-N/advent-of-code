def read_data():
    reports = []

    with open('Day2/data.txt') as f:
        numbers = f.readlines()

        for line in numbers:
            reports.append([int(n) for n in line.split()])
        
    return reports

def count_safe(reports, part=1):
    safe = 0

    for r in reports:
        if is_safe(r) or (part == 2 and is_safe_dampener(r)):
            safe += 1

    return safe


def is_safe(r):
    for i in range(len(r) - 1):
        asc = r[0] > r[1] # 1 for ascending and 0 for descenting

        if (r[i] > r[i+1]) != asc or abs(r[i] - r[i+1]) < 1 or abs(r[i] - r[i+1]) > 3:
            return False
    else:
        return True
    
    
def is_safe_dampener(r):
    for i in range(len(r)):
        if is_safe(r[:i]+r[i+1:]):
            return True
    return False


################################################
if __name__ == "__main__":
    reports = read_data()
    safe = count_safe(reports, 2)
    print (safe)