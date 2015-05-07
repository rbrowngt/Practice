class Node(object):
    def __init__(self, value):
        self.value = value
        self.adj = []

   
def bfs_iterative(node):
    #Iterative implementation
    # Assuming node contains adj list as a list
    # Also assuming node has a visited flag
    visited, stack = set(), [node]
    
    while stack:
        vertex = stack.pop()
        print vertex.value
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(vertex.adj) - visited)
            
    return visited

def bfs_recursive(node):
    return None

if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    
    a.adj.extend([b,c])
    c.adj.append(d)
    d.adj.append(a)
    
    bfs = bfs_iterative(a)
    #print bfs