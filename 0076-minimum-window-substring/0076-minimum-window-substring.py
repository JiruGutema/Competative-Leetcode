class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)

        n = len(s)
        ans = [0, len(s)]
        Window = Counter()
        left = 0
        for right in range(n):
            Window[s[right]] += 1
            
            while Window >= t:
    
                if (right-left) <= (ans[1] - ans[0]):
                    ans[0] = left
                    ans[1] = right
                if s[left] in Window:
                    Window[s[left]] -= 1
                    if Window[s[left]] == 0:
                        del Window[s[left]]
                left += 1

        if ans[1] == n:
            return ""
        return(s[ans[0]:ans[1]+1])
        
        
            



        