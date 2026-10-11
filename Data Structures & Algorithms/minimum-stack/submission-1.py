
class MinStack:

    def __init__(self):
        self.input_list = []
        self.min_list = []
        

    def push(self, val: int) -> None:
        self.input_list.append(val)

        if not self.min_list or val <= self.min_list[-1]:
            self.min_list.append(val)
        

    def pop(self) -> None:
        if  not self.input_list:
            return 
        

        last_element = self.input_list[-1]
        if last_element == self.min_list[-1]:
            self.min_list.pop()

        self.input_list.pop()
        

    def top(self) -> int:
        return self.input_list[-1] if self.input_list else -1 
        

    def getMin(self) -> int:
        return self.min_list[-1] if self.min_list else -1 

        
