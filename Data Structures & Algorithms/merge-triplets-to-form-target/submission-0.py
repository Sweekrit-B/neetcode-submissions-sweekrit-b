class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # what it boils down to essentially is
            # want to find each possible target value for every index
            # check if the combinations of those cause max to increase past the target value
        # compare pairs, and at each point, you do a failure check. 
            # since its just a max, it doesnt matter HOW much below the target any given index is, it just matters that its below the target in the first place
            # i.e. greedily deciding if its valid
        
        # example: [[1, 4, 4], [2, 5, 6], [5, 7, 5], [5, 1, 6]]
        # ix 0: [1, 4, 4]
            # 1 < 5, 4 == 4, 4 < 6
            # good to keep for now
        # ix 1: [2, 5, 6]
            # 2 < 5, 5 > 4, 6 == 6
            # cannot use
        # ix 2: [5, 7, 5]
            # 5 == 5, 7 > 4, 5 < 6
            # cannot use
        # ix 3: [5, 1, 6]
            # 5 == 5, 1 < 4, 6 == 6
            # good to use
        # final element: [5, 4, 6]

        # for every value, if every value less than or equal to the target value, then you can use it. After you have gone through the entire array, check if the final value is equal to the target

        curr_merge = [float('-inf'), float('-inf'), float('-inf')]
        for triple in triplets:
            if (triple[0] <= target[0]) and (triple[1] <= target[1]) and (triple[2] <= target[2]):
                curr_merge = [max(curr_merge[0], triple[0]), max(curr_merge[1], triple[1]), max(curr_merge[2], triple[2])]
        return curr_merge == target