class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # Step 1: Binary search to find the candidate row
        top, bottom = 0, len(matrix) - 1
        row_idx = -1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row_idx = mid
                break

        # Exit early if no row's range covers the target
        if row_idx == -1:
            return False

        # Step 2: Binary search inside the chosen row (Template B)
        row = matrix[row_idx]
        left, right = 0, len(row) - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        