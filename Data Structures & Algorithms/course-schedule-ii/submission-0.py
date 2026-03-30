class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret = []
        preMap = {cs: [] for cs in range(numCourses)}
        # Keep track of what nodes have already been solved for and what
        # Nodes you are currently solving
        visit, cycle = set(), set()

        # Build your adjacency list
        for cs, pre in prerequisites:
            preMap[cs].append(pre)
        
        def dfs(cs):
            # If this course was in your current cycle, that means,
            # you hit a cycle in the graph and completing the degree is
            # impossible
            if cs in cycle:
                return False
            # If this class has already been visited, that means we've taken it
            # So just return True
            if cs in visit:
                return True
            
            # Add the current course to the cycle and run dfs on all its prereqs.
            # If dfs returns false at any point, return False
            cycle.add(cs)
            for pre in preMap[cs]:
                if not dfs(pre):
                    return False
            cycle.remove(cs)

            # If we made it out the loop, we have no cycles, add it to the set
            # of taken courses, and add it to the output list. Return True.
            visit.add(cs)
            ret.append(cs)
            return True
        
        # Iterate through all courses and run dfs. If any dfs call returns False,
        # then it is impossible to complete the courses, so return an empty list. 
        # Otherwise, return the output list built during dfs.
        for cs in range(numCourses):
            if not dfs(cs):
                return []
        return ret
