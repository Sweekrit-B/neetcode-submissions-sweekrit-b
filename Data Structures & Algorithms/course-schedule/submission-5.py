class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # find a cycle in a graph
        prereq_dict = defaultdict(list)
        for relation in prerequisites:
            prereq_dict[relation[0]].append(relation[1])
        
        visited = set()
        branch = set()

        def dfs(node):
            if node in branch:
                return False
            if node in visited:
                return True
            
            visited.add(node)
            branch.add(node)
            for course in prereq_dict[node]:
                if not dfs(course):
                    return False
            branch.remove(node)

            return True
        
        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i):
                return False
        
        return True
