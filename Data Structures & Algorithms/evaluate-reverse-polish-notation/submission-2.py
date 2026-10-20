class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set()
        operations.add("+")
        operations.add("-")
        operations.add("*")
        operations.add("/")

        stack = []

        for c in tokens:
            if c not in operations:
                stack.append(int(c))
            else:
                n1 = stack.pop(-1)
                n2 = stack.pop(-1)
                
                if c=="+":
                    stack.append(n1+n2)
                elif c=="-":
                    stack.append(n2-n1)
                elif c=="*":
                    stack.append(n1*n2)
                elif c=="/":
                    stack.append(int(n2 / n1))

        return stack[-1]