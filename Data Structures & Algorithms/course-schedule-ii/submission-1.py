class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_deps = defaultdict(list)

        # For each prerequisite, add the pair and the individual courses
        for prereq in prerequisites:
            course_deps[prereq[0]].append(prereq[1])

        # use backtracking
        path = set()
        done = set()
        order = []

        def dfs(course):
            if course in path:
                return False # if we have already explored that path
            if course in done:
                return True # already logged that the course has gone down that path
            
            path.add(course) # add course to the path
            for prereq in course_deps[course]:
                if not dfs(prereq):
                    return False
            path.remove(course) # once you have checked every dependency, remove from path

            done.add(course) # any time this course is accessed again, we know its good already
            # print(f"Added {course} to done: {done}")
            order.append(course) # add the course to order
            # print(f"Added {course} to order: {order}")
            return True # if nothing else triggers, this is good

        for course in range(numCourses): # for every course
            if not dfs(course):
                return []
        
        return order