class Tree(object):
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.vale = value
    
    def in_order(self):
        if self.left:
            for value in self.left.in_order():
                yield value
        yield self.value
        if self.right:
            for value in self.right.in_order():
                yield value
    
    def pre_order(self):
        yield self.value
        if self.left:
            for value in self.left.pre_order():
                yield value
        if self.right:
            for value in self.right.pre_order():
                yield value
                
                
    def post_order(self):
        if self.left:
            for value in self.left.post_order():
                yield value
        if self.right:
            for value in self.right.post_order():
                yield value
                
        yield self.value