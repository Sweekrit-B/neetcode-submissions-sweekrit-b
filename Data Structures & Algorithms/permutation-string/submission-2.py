from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # smaller version of the problem
            # how do you check is s1 is a permutation of s2? if they are both the same length*
            # this is basically valid anagrams
            # most time efficient way: create a dictionary with the characters of s1 and their counts, and check whether s2 is consistent
        # now, let's zoom out to the bigger version
            # couple of things that we don't know
                # 1) where is the starting position of the permutation
                # 2) whether s2[i:i+len(s1)] is a proper permutation
            # idea:
                # iterate through s2...
                # IF ch in s2 is in s1 dict and its value is greater than 0:
                    # consider this potentially starting the perm
                    # THEN in a copy of s1 dict, we remove 1 from the ch count
                    # we can also store the length of s1 and constantly decrease that, always storing a "true" copy of these values
                    # IF the length of s1 == 0 (and this also meets the condition that we have any ch of s1 left to account for, as we are only decrementing if the value is greater than 0)
                        # return True
                # ELSE
                    # restore the "true" copy, which is just reassignment
                # move the current index forward regardless
        # does not work because each point can be a new starting point
        # however, let's reframe the problem like this
            # let's say we had two pointers, a left l and a right r
            # how do we know whether they contain a window
            # considering our first s1 dict, there are two main cases
                # if we come across a val that is in the s1 dict, we set our l
                    # then, as we move r forward, we continue to do the normal update
                    # IF r is not in s1 or the value of r in s1's copy is 0
                        # MOVE l until s2[l] == s2[r]
                        # Why? if we r is not in s1, we just move l to r. If r in s1's copy is 0, we remove the duplication that caused this in the first place
            
        s1_dict_true =  Counter(s1)
        s1_dict = s1_dict_true.copy()
        true_length = len(s1)
        remaining_length = len(s1)
        l = 0
        # print(f"Initial s1 dict: {s1_dict}")
        # print(f"Initial s1 length: {remaining_length}")

        for r in range(len(s2)):
            ch = s2[r]
            # print(f"\nLooking at character {ch}")
            if ch in s1_dict and s1_dict[ch] > 0:
                # print("We are correctly looking for a permutation!")
                s1_dict[ch] -= 1
                remaining_length -= 1
                # print(f"New s1 dict: {s1_dict}")
                # print(f"New remaining length: {remaining_length}")
                if remaining_length == 0:
                    # print("Found a permutation!")
                    return True
            else:
                # print("We are trying to get back to a valid permutation!")
                if ch not in s1_dict:
                    l = r
                    s1_dict = s1_dict_true.copy()
                    remaining_length = true_length
                else:
                    while s2[l] != ch:
                        s1_dict[ch] += 1
                        remaining_length += 1
                        l += 1
                #         print(f"New s1 dict: {s1_dict}")
                #         print(f"New remaining length: {remaining_length}")
                # print(f"Current L: {s2[l]}")
        
        return False