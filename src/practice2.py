class CWStack(object):
    pass
    
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        if self.isEmpty:
            return None
        return self.stack[len(self.stack) - 1] 
    
    def __str__(self):
        return "Stack of size: %s" % len(self.stack)
    
def reverse_str(s, stack):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    #stack.stack = list(s)
    _ = [stack.push(c) for c in list(s)]
    
    ret_str = ''
    while stack.isEmpty() == False:
        char = stack.pop()
        ret_str += char
        
    return ret_str

s = CWStack()


print reverse_str('hello', CWStack())
#test.assert_equals(reverse_str('hello', CWStack()), 'olleh') 