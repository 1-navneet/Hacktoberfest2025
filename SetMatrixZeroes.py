def setZeroes(mat):
    rows, cols = set(), set()

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                rows.add(r); cols.add(c)

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if r in rows or c in cols:
                mat[r][c] = 0
