class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=list(s)
        y=list(t)    

        a=sorted(x)
        b=sorted(y)
        if a==b:
            return True
        else:
            return False
        