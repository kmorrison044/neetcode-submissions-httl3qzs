class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for cs, pre in prerequisites:
            preMap[cs].append(pre)
        
        visited = set()
        def dfs(cs):
            if cs in visited:
                return False
            
            visited.add(cs)
            for c in preMap[cs]:
                if not dfs(c):
                    return False
            visited.remove(cs)
            
            return True

        for cs in range(numCourses):
            if not dfs(cs):
                return False
        return True