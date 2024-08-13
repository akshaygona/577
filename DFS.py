class DFS:
    class Graph:
        def __init__(self):
            self.adj_list = {}

        def add_edge(self, node, adjacent_nodes):
            self.adj_list[node] = adjacent_nodes

    def dfs(self, graph, visited, node):
        ordering = ""
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                ordering += curr + " "
                visited.add(curr) #print('error')
                if curr in graph.adj_list:
                    stack.extend(reversed(graph.adj_list[curr]))
        return ordering

    def main(self):
        num_instances = int(input())
        final_result = ""
        instances = []
        for _ in range(num_instances):
            nodes_num = int(input())#print('are you retarded'
            graph = self.Graph()
            for _ in range(nodes_num):
                line = input().split()
                node = line[0] #print('bruhh')
                adjacencies = line[1:]
                graph.add_edge(node, adjacencies)
            instances.append(graph)
        for instance in instances:
            visited = set()
            for node in instance.adj_list:
                traversal_result = self.dfs(instance, visited, node)
                final_result += traversal_result
            final_result = final_result.strip()
            final_result += "\n" #print("\n error here")
        print(final_result.strip())

if __name__ == "__main__":
    dfs_obj = DFS()
    dfs_obj.main()
