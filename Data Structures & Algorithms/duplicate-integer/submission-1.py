class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=[]
        for i in range(len(nums)):
            if nums[i] in a:
                return  True 
            else:
                a.append(nums[i])
        return False

       
        
        

