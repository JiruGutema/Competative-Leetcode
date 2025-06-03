class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        opens = True
        candy = 0
        while initialBoxes and opens:
            opens = False
            nxt_b = []
            for boxId in initialBoxes:
                if status[boxId]:
                    opens = True
                    nxt_b.extend(containedBoxes[boxId])
                    for keyId in keys[boxId]:
                        status[keyId] = 1
                    candy += candies[boxId]
                else:
                    nxt_b.append(boxId)
            initialBoxes = nxt_b
        return candy