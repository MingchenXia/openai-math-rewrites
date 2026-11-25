from itertools import product
from math import comb
from random import Random


def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        for j in range(row + 1, len(a)):
            if not a[j][col]:
                continue
            multiple = a[j][col] * inv
            for k in range(col, len(a[j])):
                a[j][k] = (a[j][k] - multiple * a[row][k]) % p
        row += 1
        if row == len(a):
            break
    return row


jet_cases = 0
for p in (2, 3, 5, 7):
    for n, m in product(range(1, 4), range(4)):
        transverse = [t for t in product(range(m + 1), repeat=n - 1) if sum(t) <= m]
        for r in range(1, min(p, 5)):
            source = [(beta, b) for beta in transverse for b in range(r * (m + 1 - sum(beta)))]
            target = [(i, alpha, j) for i in range(1, r + 1) for alpha in transverse
                      for j in range(m + 1 - sum(alpha))]
            assert len(source) == len(target)
            matrix = []
            for i, alpha, j in target:
                row = []
                for beta, b in source:
                    coefficient = comb(b, j) * pow(i, b-j, p) if b >= j else 0
                    for u, v in zip(beta, alpha):
                        coefficient *= comb(u, v)
                    row.append(coefficient)
                matrix.append(row)
            assert rank_mod(matrix, p) == len(target), (p, n, m, r)
            jet_cases += 1

p = 101
rng = Random(39)
row_cases = 0
for q, m, _ in product(range(1, 4), range(1, 7), range(5)):
    sizes = sorted((rng.randint(1, m) for _ in range(q*m)), reverse=True)
    sizes = [min(size, m - i//q) for i, size in enumerate(sizes)]
    heights = rng.sample(range(p), len(sizes))
    points = [(j, h) for h, size in zip(heights, sizes) for j in rng.sample(range(p), size)]
    polynomials = [(i, b) for i, size in enumerate(sizes) for b in range(size)]
    matrix = []
    for j, h in points:
        vals = [1]
        for a in heights:
            vals.append(vals[-1] * (h-a) % p)
        matrix.append([vals[i] * pow(j, b, p) for i, b in polynomials])
    assert rank_mod(matrix, p) == len(points), (q, m, sizes)
    row_cases += 1

print(f"{jet_cases} full-rank stretched-simplex jet examples, {row_cases} full-rank horizontal-row examples")
