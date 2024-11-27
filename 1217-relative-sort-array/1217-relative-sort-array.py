class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        ans = []
        counter = 0
        while counter < len(arr2):
            curr = arr2[counter]
            
            for i in arr1[:]:  
                if i == curr:
                    ans.append(i)
                    arr1.remove(i)
            counter += 1
        

        arr1.sort() 
        
        ans.extend(arr1[:])
        return ans