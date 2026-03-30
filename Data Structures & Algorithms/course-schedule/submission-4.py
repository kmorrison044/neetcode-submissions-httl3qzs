class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # First map the classes to the prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for cs, pre in prerequisites:
            preMap[cs].append(pre)

        # Define a visited set that will track if you already visited a class
        # during a dfs. If so, that means you hit a cycle in the class requirements.    
        visited = set()
        def dfs(cs):
            # Check if the class is already in visited. If so, then we
            # have cyclical requirements
            if cs in visited:
                return False

            # Check if we have already verified that there are no cycles down
            # this path. If not, we can return True.
            if preMap[cs] == []:
                return True
            
            # Add the current class to visited
            visited.add(cs)
            # Loop through the classes preqs and ensure
            # That there are no cycles by calling dfs. If dfs
            # Returns false, then return false to break out of the loop and
            # recursion
            for c in preMap[cs]:
                if not dfs(c):
                    return False

            # Remove the current class from visited so that it can be used for other class preqs
            visited.remove(cs)

            # If it passed the loop, then set the list of prereqs
            # for this class to empty, since we know this path is good,
            # then return True.
            preMap[cs] = []
            return True

        # Check every class and see if it passed dfs. If so, return true, otherwise
        for cs in range(numCourses):
            if not dfs(cs):
                return False
        return True