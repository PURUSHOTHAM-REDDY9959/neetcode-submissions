class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            
            else:  # closing bracket
                if not stack:
                    return False
                
                last = stack.pop()
                
                if (i == ')' and last != '(') or \
                   (i == '}' and last != '{') or \
                   (i == ']' and last != '['):
                    return False
        
        return not stack
