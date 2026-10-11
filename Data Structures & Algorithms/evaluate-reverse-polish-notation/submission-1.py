class Solution:
    
    def add(self, *kwargs):
        s = 0 
        for each in kwargs:
                s += each
        return s

    def mul(self, *kwargs):
        curr = 1 
        for each in kwargs:
                curr *= each 
        return curr 

    def sub(self, *kwargs):
        curr = kwargs[0]
        for each in kwargs[1:]:
                curr -= each 
        return curr 

    def divide(self, *kwargs):
        curr = kwargs[0]
        for each in kwargs[1:]:
            curr = int(curr / each)
        return curr

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mapper = {
                "+": self.add, 
                "-": self.sub, 
                "*": self.mul,
                "/": self.divide
        }

        for ch in tokens:
                if ch not in mapper:
                        stack.append(int(ch))
                else:
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(
                            mapper[ch](a,b)
                        )
        return stack[-1]

        