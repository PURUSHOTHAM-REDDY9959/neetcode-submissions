class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in s:
            if i.isalnum()==True:
                i=i.lower()
                a.append(i)
        if a==list(reversed(a)):
            return True
        return False
