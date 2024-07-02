Sample = [
 [".",".",".",".",".",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,["9","3",".",".","2",".","4",".","."]
,[".",".","7",".",".",".","3",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".","3","4",".",".",".","."]
,[".",".",".",".",".","3",".",".","."]
,[".",".",".",".",".","5","2",".","."]]

from collections import Counter
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        checkboard = []

        for down in range(0,6,3):
            for left in range(0,6,3):
                for y in range(3):
                    for x in range(3):
                        if board[y+down][x+left] in checkboard and board[y+down][x+left] != ".":
                            return False
                        else:
                            checkboard.append(board[y+down][x+left])
                c = dict(Counter(checkboard))
                try:
                    c.pop(".")
                except:
                    pass
                for z in list(c.values()):
                    if z >= 2:
                        return False
                checkboard = []
        
        for i in range(9):
            c = dict(Counter(board[i]))
            c.pop(".")
            for x in list(c.values()):
                if x >= 2:
                    return False
            
            hold = [board[0][i],board[1][i],board[2][i],board[3][i],board[4][i],board[5][i],board[6][i],board[7][i],board[8][i]]
            c = dict(Counter(hold))
            c.pop(".")
            for x in list(c.values()):
                if x >=2:
                    return False
            

        return True
        

#unsubmitted, I feel like I'm close but I've been working on this for an hour and a half so I think its about time to pack it up and work on something else

if __name__ == '__main__':
    hold = (Solution.isValidSudoku(None,Sample))
    print (hold)