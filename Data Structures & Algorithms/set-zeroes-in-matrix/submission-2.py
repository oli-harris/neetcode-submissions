class Solution:
    # matrix
    # [[2, 4],
    #  [1, 4]]

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        zeros = []

        # finds zeros
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeros.append((row, col))

        # replaces whole row and col in-place
        for zero in zeros:
            row, col = zero[0], zero[1]

            # replace col, loop through rows
            for r in range(m):
                matrix[r][col] = 0

            # replace row, loop through columns
            for c in range(n):
                matrix[row][c] = 0