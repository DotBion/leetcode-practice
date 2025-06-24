# Last updated: 6/24/2025, 7:48:29 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #step1: swap i,j for only the upper right triangular elements: if done for all will reposition them back tothe prev position
        l = len(matrix[0])
        for i in range(l) :
            for j in range(l) :
                if j>=i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        #step2: take mirror image of each row
        for i in range(l) :
            right = l-1
            for j in range(l//2) :
                matrix[i][j], matrix[i][right] = matrix[i][right], matrix[i][j]
                right-=1
                

                