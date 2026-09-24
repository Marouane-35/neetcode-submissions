import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda a, b: int(a / b)
}
        stack=[]
        for el in tokens :
            if el in ops :
                a=stack.pop()
                b=stack.pop()
                stack.append(ops[el](b,a))
            else:  
                stack.append(int(el))
        return stack[0]