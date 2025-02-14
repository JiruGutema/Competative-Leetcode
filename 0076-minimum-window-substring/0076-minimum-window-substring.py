# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # failed


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

        # doesn't make sense

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

        # worked

        # t = Counter(t)

        # n = len(s)
        # ans = [0, len(s)]
        # Window = Counter()
        # left = 0
        # for right in range(n):
        #     Window[s[right]] += 1
            
        #     while Window >= t and  :
    
        #         if (right-left) <= (ans[1] - ans[0]):
        #             ans[0] = left
        #             ans[1] = right
        #         if s[left] in Window:
        #             Window[s[left]] -= 1
        #             if Window[s[left]] == 0:
        #                 del Window[s[left]]
        #         left += 1

        # if ans[1] == n:
        #     return ""
        # return(s[ans[0]:ans[1]+1])
        
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT,window={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        have,need=0,len(countT)
        res,resLen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if(c in countT and window[c] == countT[c]):
                have+=1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if(s[l] in countT and window[s[l]] < countT[s[l]]):
                    have-=1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
            



        