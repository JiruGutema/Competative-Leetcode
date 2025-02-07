class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n=len(queries)
        ic = defaultdict(int)
        colors = defaultdict(int)
        ans=[1]
        ic[queries[0][0]]=queries[0][1]
        colors[queries[0][1]]+=1
        for [x,y] in queries[1:]:
            cur = ic[x]
            ic[x]=y
            k=0
            colors[cur]-=1
            if colors[cur]==0:
                k-=1
                del colors[cur]
            colors[y]+=1
            if colors[y]==1:
                k+=1
            ans.append(ans[-1]+k)
        return ans


                