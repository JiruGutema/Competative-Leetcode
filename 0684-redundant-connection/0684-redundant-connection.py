class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(node):
            par = parent[node]
            
            while par != parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]
            return par

        def union(node_1, node_2):
            par_node_1 = find(node_1)
            par_node_2 = find(node_2)

            if par_node_1 == par_node_2:
                return False
            
            parent[par_node_1] = par_node_2

            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        return []

            