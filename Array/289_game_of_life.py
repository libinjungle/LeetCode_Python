class Solution(object):
    def gameOfLife(self, board):
        """
        count how many live neigbor cells each cell has. mark dead cell that can be updated as 2 and live cell
        that can be updated as 3
        Note: the game rule is to update at the same time. so we can not update a cell even if it can be updated
        when it is its turn.
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
          for j in range(n):
            num_neighbor = sum([board[a][b]%2 for a in range(i-1, i+2) for b in range(j-1, j+2)
                                if 0<= a<m and 0<=b<n]) - board[i][j]
            if board[i][j] == 0 and num_neighbor == 3:
              board[i][j] = 2
            if board[i][j] == 1 and (num_neighbor < 2 or num_neighbor > 3):
              board[i][j] = 3
        for i in range(m):
          for j in range(n):
            if board[i][j] == 2:
              board[i][j] = 1
            if board[i][j] == 3:
              board[i][j] = 0







