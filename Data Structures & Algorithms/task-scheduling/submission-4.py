import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        run = [] # max heap -> (-no. runs, "letter", time)
        cooldown = [] # min heap -> (time, "letter", -no. runs)

        # push all items into run
        tasks_enumerate = defaultdict(int)
        for task in tasks:
            tasks_enumerate[task] += 1
        for task in tasks_enumerate:
            heapq.heappush(run, (-tasks_enumerate[task], 0))

        t = 0
        # print(f"Run: {run}, cooldown: {cooldown}, t: {t}")
        while len(run) > 0 or len(cooldown) > 0:
            # Dealing with the run queue
            if run:
                # grab the most pressing element to be run
                priority_elem = heapq.heappop(run)
                if priority_elem[0] + 1 != 0:
                    # update and push
                    heapq.heappush(cooldown, (t + n, priority_elem[0] + 1))
            
            # Dealing with the cooldown queue
            if cooldown:
                # add any waiting cooldown elements back into the run queue
                while cooldown and cooldown[0][0] == t:
                    next_waiting = heapq.heappop(cooldown) # officially pop the element
                    # update and push
                    heapq.heappush(run, (next_waiting[1], next_waiting[0]))
            
            t += 1
            # print(f"Run: {run}, cooldown: {cooldown}, t: {t}")
        
        # print(f"Run: {run}, cooldown: {cooldown}, final time: {t}")
        return t
            