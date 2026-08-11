import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position: [1, 4], speed: [3, 2]
        # how do we determine the frontrunner? -> current max
        # frontrunner = 4, speed = 2 -> new position = 6
            # update; position: [4, 6] -> f = 0
        # frontrunner = 6, speed = 2 -> new position = 8
            # update; position: [7, 8] -> f = 0
        # frontrunner = 8, speed = 2 -> new position = 10
            # update; position: [10, 10] -> f = 1
        
        # position: [4, 1, 0, 7], speed: [2, 2, 1, 1]
        # stack: [0, 1, 4, 7], speed: [1, 2, 2, 1]
        # time = 1
            # stack: [1, 3, 6, 8] -> f = 0
        # time = 2
            # stack: [2, 5, 8, 9] -> f = 0
        # time = 3
            # stack: [3, 7, 10, 10] -> f = 1
        # time = 4
            # stack: [4, 9, 10, 10] -> f = 1
    
        # positions: [7, 4, 1, 0], speeds: [1, 2, 2, 1]
        # time: [3, 2, 5, 10] -> car 1 takes 3 tu, car 2 takes 2, ...
        # example: [3, 2, 5, 10, 2] -> what do we notice?
            # ix 1 will reach the car at ix 0
            # ix 4 will reach the car at ix 3
        # essentially, we are counting how many "decreasing" sequences there are in the array
            # monotonic decreasing stack
            # [3, 2] --> f = 1
            # add 5, clear --> [5] --> f = 2
            # add 10, clear --> [10] --> f = 3
            # add 2 --> [10, 2]
            # can also solve using arrays and doing a simple loop
        
        # what if we did it in the opposite order
        # time: [2, 10, 11, 5, 2, 3]
        # monotonic increasing stack
            # [2, 10, 11] --> f = 1
            # [5] --> f = 2
            # [2, 3] --> f = 3
        # however, a monotonic increasing stack breaks under some cases
            # ex. if time taken was [5, 3, 6]
            # then, then considering the MIS, we would have 2 fleets
            # however, in actuality, 5 falls under 6
        # does this work in the opposite direction?
            # [6, 3] --> add 5, get [6, 5] --> add 10, get [10] --> add a fleet when the stack is empty
        
        sorted_position, sorted_speed = zip(*sorted(zip(position, speed)))
        # print(f"Sorted positions: {sorted_position}")
        # print(f"Sorted speeds: {sorted_speed}")
        time_taken = [(target - sorted_position[i])/sorted_speed[i] for i in range(len(sorted_position))]
        # print(f"Time taken: {time_taken}")
        cur_max = 0
        fleets = 0
        for i in range(len(time_taken)-1, -1, -1):
            if time_taken[i] > cur_max:
                fleets += 1
                cur_max = time_taken[i]
        return fleets


