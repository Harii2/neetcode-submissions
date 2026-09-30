from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        path = set()
        done = set()

        def dfs(course):

            # Cycle
            if course in path:
                return False

            # Already checked
            if course in done:
                return True

            path.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            path.remove(course)

            done.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True