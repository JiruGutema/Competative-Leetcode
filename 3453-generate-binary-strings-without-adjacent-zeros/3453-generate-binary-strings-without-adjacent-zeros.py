class Solution:
    def validStrings(self, n: int) -> List[str]:
        # if n == 1:
        #     return ["0", "1"]
        ans, path = [], []


        def backtrack(idx):
            if idx == n:
                ans.append((path[:]))
                return

            path.append("1")
            backtrack(idx+1)
            path.pop()

            if idx == 0:
                path.append("0")
                backtrack(idx+1)
                

            if path and path[-1] == "1":
                path.append("0")
                backtrack(idx+1)
                path.pop()

        backtrack(0)

                
        
        



        return ["".join(path) for path in ans]
