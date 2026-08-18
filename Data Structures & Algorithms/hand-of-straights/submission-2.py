class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # [1,2,4,2,3,5,3,4], group size = 4
        # {1: 1, 2: 2, 3: 2, 4: 2, 5: 1}
        # starting at 1, can we make a sequence of 4?
            # yes? then update
        # {1: 0, 2: 1, 3: 1, 4: 1, 5: 1}
        # starting at 2, can we make a sequence of 4?
            # yes? then update
        # worst case time complexity: O(n + nk) = O(nk), where n is the size of the hand and k is the group size

        # is there a way to do this in O(n) time?
        # key requirement: a data structure that is able to (1) have duplicates, (2) have O(1) add, search, and delete
                # if we use a dictionary, we can store how many are at which endpoint
        # strategy 1: what if we sorted?
            # [1, 2, 2, 3, 3, 4, 4, 5]
            # hands dict: {}
            # ix 0: is 0 in the dict?
                # no: hands dict: {1: [1]}
            # ix 1: is 1 in the dict?
                # yes: hands dict: {1: None, 2: [2]} -> del 1 -> {2: [2]}
            # ix 2: is 1 in the dict?
                # no: hands dict: {2: [2, 1]}
            # ix 3: is 2 in the dict?
                # yes: hands dict: {2: [2], 3: [2]}
            # ix 4: is 2 in the dict?
                # yes: hands dict: {2: None, 3: [2, 3]} -> del 2 -> {3: [2, 3]}
            # ix 5: is 3 in the dict?
                # yes: hands dict: {3: [3], 4: [3]}
            # ix 6: is 3 in the dict?
                # yes: hands dict: {3: None, 4: [3, 4]} -> del 3 -> {4: [4, 3]}
            # ix 7: is 4 in the dict?
                # yes: hands dict: {4: [4], 5: [4]}
            # final answer = are all values in hands dict the same as group size?
                # maybe we use a heap, to always use the current smallest straight length to try to normalize
        
        hand.sort()
        hands_dict = defaultdict(list)
        
        for card in hand:
            if card-1 not in hands_dict:
                heapq.heappush(hands_dict[card], 1)
                # print(hands_dict)
            else:
                min_straight_length = hands_dict[card-1][0]
                # need to add a conditional - if the min straight length is equal to  group size, then need to skip this process
                if min_straight_length == groupSize:
                    heapq.heappush(hands_dict[card], 1)
                    # print(hands_dict)
                else:
                    heapq.heappop(hands_dict[card-1])
                    hands_dict[card].append(min_straight_length + 1)
                    if not hands_dict[card-1]:
                        del hands_dict[card-1]
                    # print(hands_dict)
        
        all_hand_sizes = set()
        for hands in hands_dict.values():
            all_hand_sizes.update(hands)
        
        return len(all_hand_sizes) == 1 and list(all_hand_sizes)[0] == groupSize