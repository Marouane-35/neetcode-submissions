class Solution:
    def isValid(self, s: str) -> bool:
        first=['(','{','[']
        last=[')','}',']']
        stack=[]
        for el in s :
            if el in first :
                stack.append(el)
            else :
                if stack and last.index(el)==first.index(stack[-1]) :
                    stack.pop()
                else :
                    return False
        return not stack 
           
        