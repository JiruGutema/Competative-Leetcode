class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = []
        loser = []

        n = len(matches)
        for match in matches:
            winner.append(match[0])
            loser.append(match[1])
            
        winner = Counter(winner)
        loser = Counter(loser)
        win = []
        lose = []

        for k, v in winner.items():
            lost = loser.get(k, 0)
            if lost == 0:
                win.append(k)
        for k, v in loser.items():
            if v == 1:
                lose.append(k)
        win.sort()
        lose.sort()
        return [win, lose]
        