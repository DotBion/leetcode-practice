# Last updated: 7/29/2025, 5:48:35 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        print(rows,cols)
        searchRow = -1
        left = 0#1
        right = rows-1
        #get row index
        while left<=right :
            mid = (left+right)//2
            if target == matrix[mid][0] :
                return True
            #elif target>= matrix[mid-1][0] and target < matrix[mid][0] :
            elif target > matrix[mid][0] and target <= matrix[mid][cols-1]:
                searchRow = mid
                break#or make left>right
            elif target > matrix[mid][0] :
                left = mid+1
            elif target < matrix[mid][0] :
                right = mid-1

        if rows-1 == 0 :
            searchRow = 0
        elif searchRow == -1 :
            return False

        left = 0
        right = cols - 1
        #get column index
        while left<=right :
            mid = (left+right)//2 
            if target == matrix[searchRow][mid] :
                return True
            elif target > matrix[searchRow][mid] :
                left = mid+1
            elif target < matrix[searchRow][mid] :
                right = mid-1
        
        return False

