Sample = ["4","13","5","/","+"]
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = ["+","-","/","*"]
        answer = 0
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                if i == "+":
                    for o in stack:
                        answer+=int(o)
                if i == "-":
                    for o in stack:
                        answer-=int(o)
                if i == "*":
                    for o in stack:
                        answer*=int(o)
                if i == "/":
                    for o in stack:
                        answer//=int(o)
                stack.clear()
        return answer





if __name__ == '__main__':
    hold = (Solution.evalRPN(None,Sample))
    print (hold)