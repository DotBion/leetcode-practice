class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        #cant revisit the same character in our path
        path = set()
        if len(word) > rows * cols:
            return False
        board_count = Counter(ch for row in board for ch in row)
        for ch, need in Counter(word).items():
            if board_count[ch] < need:           # missing letters
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]   
        
        
        def dfs(r, c, i):
            #pos of board and curr char of the target i is the index at word
            if i == len(word) :
                return True
            #check invalid - char in word is not equal to the one at board or char already visited in path
            if r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path :
                return False
        
            #now we found the char that we'ere looking for
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            path.remove((r,c)) #cleanup since we are returning
            return res

        #brute force for every single staring positon run dfs
        for r in range(rows) :
            for c in range(cols) :
                if dfs(r,c,0): return True
        
        return False
        #TC : O(n*m*dfs) = O(n*m*(4^len(word))) since we are calling dfs 4 times