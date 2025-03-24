class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:  
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
     
        return sum(arr[i] * left[i] * right[i] for i in range(n)) % MOD



# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         res = []
#         path = []

#         def backtrack(start, end):
#             if end > len(arr):
#                 return
#             res.append(arr[start:end])
#             backtrack(start, end+1)

#         for i in range(len(arr)):
#             backtrack(i, i+1)


#         for i in res:
#             path.append(min(i))
#         tot = 0
#         for i in path:
#             tot += i
#         return tot           
