class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def helper(nd,k,dt):
            return sum(1 for d in dt[nd] if d<=k)
        n=len(edges1)
        m=len(edges2)
        t1=[[] for _ in range(n+1)]
        t2=[[] for _ in range(m+1)]
        
        for u,v in edges1:
            t1[u].append(v)
            t1[v].append(u)
        # print(t1)
        for u,v in edges2:
            t2[u].append(v)
            t2[v].append(u)
        # print(t2)
        d1=[[math.inf for _ in range(n+1)] for i in range(n+1)]
        d2=[[math.inf for _ in range(m+1)] for i in range(m+1)]

        # breadth first search
        for i in range(n+1):
            vis=[False]*(n+1)
            q1=deque([(i,0)])
            vis[i]=True
            while q1:
                nd=q1.popleft()
                d1[i][nd[0]]=nd[1]
                for v in t1[nd[0]]:
                    if not vis[v]:
                        q1.append((v,nd[1]+1))
                        vis[v]=True

        # breadth first search
        for i in range(m+1):
            vis=[False]*(m+1)
            q1=deque([(i,0)])
            vis[i]=True
            while q1:
                nd=q1.popleft()
                d2[i][nd[0]]=nd[1]
                for v in t2[nd[0]]:
                    if not vis[v]:
                        q1.append((v,nd[1]+1))
                        vis[v]=True
        
        res=[0]*(n+1)
        # print(res)
        rmt=0

        # iterate and search for valid
        for j in range(m+1):
            rt2=helper(j,k-1,d2)
            rmt=max(rmt,rt2)
            
        for i in range(n+1):
            mr=0
            rt1=helper(i,k,d1)
            res[i]=rt1+rmt
        return res
                
        
        