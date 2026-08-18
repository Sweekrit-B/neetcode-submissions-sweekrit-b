class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # "xyxxyzbzbbisl"
        # {x: 3, y: 2, z: 2, b: 3, i: 1, s: 1, l: 1}
        # essentially, want to build substring from start until all instances of each contained letter has appeared
        # then, want to move to the next
        # temp = {}
        # ix = 0 -> x -> temp = {x: 1}
        # ix = 1 -> y -> temp = {x: 1, y: 1}
        # ix = 2 -> x -> temp = {x: 2, y: 1}
        # ix = 3 -> x -> temp = {x: 3, y: 1}
        # ix = 4 -> y -> temp = {x: 3, y: 2} -> for every value in temp, its equal to every value in the counter -> therefore, split this off

        # counter = {z: 2, b: 3, i: 1, s: 1, l: 1}
        # same process for the rest

        # max dictionary size is 26 -> O(26) operation for update, O(n) to go thorugh the string -> O(n) overall

        counts = Counter(s)
        temp = defaultdict(int)
        curr_string = ""
        res = []
        
        for ch in s:
            temp[ch] += 1
            curr_string += ch
            # print(f"Temp: {temp}")
            # print(f"Current string: {curr_string}")
            
            consistent = True
            for letter in temp:
                if temp[letter] != counts[letter]:
                    consistent = False
            
            # if everything is good to go...
            if consistent:
                res.append(len(curr_string))
                curr_string = ""
                temp = defaultdict(int)
        
        return res
                