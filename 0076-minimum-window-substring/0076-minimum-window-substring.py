class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ans = ""
  
        
        # if len(s) < len(t):
        #     return ans
        # if len(t) ==1 and t in s:
        #     return t
        # if len(t) == len(s) and t in s:
        #     return t
      
        # for start in range(len(s)):
            
        #     for end in range(len(s)+1):
                
        #         boolean = True
        #         for i in t:
        #             if i not in s[start:end]:
        #                boolean = False
                    
        #         if ans and boolean and len(ans) >= len(s[start:end]):
        #             ans = s[start:end]  
        #         elif boolean:
        #             ans = s[start:end]   
                        
        # return ans

        # dictionary = {}
        # count= Counter(t)
        # i = 0
        # j = 0
        # index = []
        # while j < len(s):
        #     if s[j] in count:
        #         dictionary[s[j]] = 1
        #     if count == dictionary:
        #         if index:
        #             if index[1] - index[0] > j-i:
        #                 index[0] = i
        #                 index[1] = j
        #         else:
        #             index.append(i)
        #             index.append(j)

                 
        #         dictionary.clear()
        #         i = j
        #     j += 1
        # return s[index[0]:index[1]-1]

        t = Counter(t)

        n = len(s)
        ans = [0, len(s)]
        Window = Counter()
        left = 0
        for right in range(n):
            Window[s[right]] += 1
            
            while Window >= t :
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
            
            



        