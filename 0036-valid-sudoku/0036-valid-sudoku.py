class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                element = board[i][j]

                if element == ".":
                    continue
                if element in row[i] or element in col[j] or element in box[i//3, j//3]:
                    return False
                row[i].add(element)
                col[j].add(element)
                box[i//3, j//3].add(element)
        return True
