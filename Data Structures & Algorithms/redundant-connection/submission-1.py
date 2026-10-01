class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [ i for i in range(len(edges) + 1)]

        def find(x):
            if parent[x] == x:
                return x 
            parent[x] = find(parent[x])
            return find(parent[x])
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False 
            
            parent[root_a] = root_b
        
            return True 
        
        for a,b in edges:
            if not union(a, b):
                return [a, b]
        