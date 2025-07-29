# Last updated: 7/29/2025, 5:48:08 PM
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        cij = dict.fromkeys(range(len(mat)),0)
        cik = dict.fromkeys(range(len(mat[0])),0)
        rowindex = [0]*(len(mat)*len(mat[0])+1)
        colindex = [0]*(len(mat)*len(mat[0])+1)
        #preprocess
        print(rowindex)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rowindex[mat[i][j]] = i
                colindex[mat[i][j]] = j
        print(cij)
        print(cik)

        for i in range(len(arr)) :
            cij[rowindex[arr[i]]]+=1
            cik[colindex[arr[i]]]+=1
            if cij[rowindex[arr[i]]] == len(mat[0]) or cik[colindex[arr[i]]] == len(mat) :
                return i
        
        # for i in range(len(arr)):
        #     for j in range(len(mat)):
        #         for k in range(len(mat[j])):
        #             if arr[i] == mat[j][k] :
        #                 cij[j]+=1
        #                 cik[k]+=1
        #             if cij[j] == len(mat[0]) or cik[k] == len(mat) :
        #                 return i
        return False

