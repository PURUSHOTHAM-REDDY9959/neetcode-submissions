class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=height
        z=0
        c=0
        for i in range(len(a)):
            for j in range(1,len(a)):
                if a[i]>a[j]:
                    b=len(a[i:j])
                    c=b*a[j]
                else:
                    d=len(a[i:j])
                    c=d*a[i]
                z=max(z,c)
        return z
