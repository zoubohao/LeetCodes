from typing import List
import numpy as np

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        boxes = {i:set() for i in range(9)}
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != ".":
                    if ele not in rows[i]: rows[i].add(ele)
                    else: return False
                    if ele not in cols[j]: cols[j].add(ele)
                    else: return False
                    if i // 3 == 0:
                        if j // 3 == 0:
                            if ele not in boxes[0]:
                                boxes[0].add(ele)
                            else:
                                return False
                        elif j // 3 == 1:
                            if ele not in boxes[1]:
                                boxes[1].add(ele)
                            else:
                                return False
                        elif j // 3 == 2:
                            if ele not in boxes[2]:
                                boxes[2].add(ele)
                            else:
                                return False
                    elif i // 3 == 1:
                        if j // 3 == 0:
                            if ele not in boxes[3]:
                                boxes[3].add(ele)
                            else:
                                return False
                        elif j // 3 == 1:
                            if ele not in boxes[4]:
                                boxes[4].add(ele)
                            else:
                                return False
                        elif j // 3 == 2:
                            if ele not in boxes[5]:
                                boxes[5].add(ele)
                            else:
                                return False
                    elif i // 3 == 2:
                        if j // 3 == 0:
                            if ele not in boxes[6]:
                                boxes[6].add(ele)
                            else:
                                return False
                        elif j // 3 == 1:
                            if ele not in boxes[7]:
                                boxes[7].add(ele)
                            else:
                                return False
                        elif j // 3 == 2:
                            if ele not in boxes[8]:
                                boxes[8].add(ele)
                            else:
                                return False
        return True



if __name__ == "__main__":
    a =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print(s.isValidSudoku(a))
