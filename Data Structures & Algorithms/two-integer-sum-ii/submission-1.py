class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        for i,j in enumerate(numbers):
            target1=target-j
            for z in range(1,len(numbers)):
                if numbers[z]==target1:
                    a.append(i+1)
                    a.append(z+1)
                    return a
           