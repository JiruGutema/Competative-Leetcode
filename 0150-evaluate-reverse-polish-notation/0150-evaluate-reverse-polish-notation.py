class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if len(stack)>=2 and i in "*/-+":
                first = stack.pop()
                second = stack.pop()
                if i == "*":
                    stack.append((second*first))
                elif i == "-":
                    stack.append((second-first))
                elif i == "+":
                    stack.append((second+first))
                elif i == "/":
                    stack.append(int(second/first))
            else:
                stack.append(int(i))
        return stack[0]


                
