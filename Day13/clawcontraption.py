import re
import numpy as np

def read_data():
    with open('Day13/data.txt') as f:
        content = f.read()

    blocks = content.strip().split("\n\n")
    
    results = []
    
    for block in blocks:
        a = [[int(x), int(y)] for x, y in re.findall(r"Button \w: X\+(\d+), Y\+(\d+)", block)]
        
        b = [[int(x), int(y)] for x, y in re.findall(r"Prize: X=(\d+), Y=(\d+)", block)][0]
        
        results.append((np.array(a).T, np.array(b)))
    
    return results

def solve1(data):
    tokens = 0
    for a, b in data:
        x = np.linalg.solve(a,b)

        if np.allclose(x, np.round(x)) and np.all(x <= 100):
            x = np.round(x).astype(int)
            tokens += 3*x[0] + x[1]

    return tokens

def solve2(data):
    tokens = 0
    for a, b in data:
        x = np.linalg.solve(a,b+10000000000000)

        if np.allclose(x, np.round(x), atol=1.0e-17, rtol=1.0e-14):
            x = np.round(x).astype(int)
            tokens += 3*x[0] + x[1]

    return tokens

if __name__ == "__main__":
    data = read_data()
    print(solve1(data))
    print(solve2(data))
