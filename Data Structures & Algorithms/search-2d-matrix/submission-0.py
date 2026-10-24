class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [element for row in matrix for element in row]

        left = 0
        right = len(flattened) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if flattened[mid] < target:
                left = mid + 1
            elif flattened[mid] > target:
                right = mid - 1
            else:
                # m, n = len(matrix), len(matrix[0])
                # position = [mid // n, mid % n]
                return True

        return False


