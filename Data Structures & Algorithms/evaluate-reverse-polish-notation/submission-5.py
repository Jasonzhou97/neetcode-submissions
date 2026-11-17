class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        queue = deque([])
        operators = set()
        operators.add("+")
        operators.add("-")
        operators.add("*")
        operators.add("/")

        i = 0
        while i < len(tokens):
            cur = tokens[i]
            if cur in operators:
                num1 = queue.pop()
                num2 = queue.pop()
                if cur=="+":
                    queue.append(num1+num2)
                elif cur=="-":
                    queue.append(num2-num1)
                elif cur=="*":
                    queue.append(num2*num1)
                elif cur=="/":
                    queue.append(int(num2/num1))
            else:
                queue.append(int(cur))
            i += 1

        return queue.pop()