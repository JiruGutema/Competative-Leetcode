class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        
        while a > 0 or b > 0:
            if a > b:  
                if a >= 2:  
                    ans.append("aa")
                    a -= 2
                else:
                    ans.append("a")
                    a -= 1
                
                if b > 0:  
                    ans.append("b")
                    b -= 1
            
            elif b > a:  
                if b >= 2:  
                    ans.append("bb")
                    b -= 2
                else:
                    ans.append("b")
                    b -= 1
                
                if a > 0:  
                    ans.append("a")
                    a -= 1
            
            else:  
                ans.append("a")
                ans.append("b")
                a -= 1
                b -= 1

        return "".join(ans)
