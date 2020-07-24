class Stack():

    def __init__(self):
        self.values = []

    def push(self, el):
        return self.values.append(el)

    def pop(self):
        val = self.values[-1]
        del self.values[-1]
        return val

    def peek(self):
        return self.values[-1]

    def is_empty(self):
        if len(self.values)>0:
            return False
        else:
            return True