class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for i in s:
            # opening bracket
            if i in mapping.values():
                stack.append(i)
            
            # closing bracket
            elif i in mapping:
                if not stack:
                    return False
                
                top = stack.pop()
                
                if top != mapping[i]:
                    return False
        
        return len(stack) == 0
