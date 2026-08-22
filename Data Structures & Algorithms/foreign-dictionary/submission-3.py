class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # step 0: deal with edge cases
        if len(words) == 0: return ""
        if len(words) == 1: return words[0]

        # helper function to detect cycles
        def is_cycle(start, node):
            if node == start:
                return True
            
            for neighbor in self.adj_list[node]:
                if is_cycle(start, neighbor):
                    return True
            
            return False
        
        # step 1: build the adjacency list
        self.adj_list = defaultdict(list)
        self.all_chs = set()
        
        for ix in range(len(words)-1):
            # find the current word and the next word
            curr_word = words[ix]
            next_word = words[ix+1]
            # print(f"Dealing with {curr_word} and {next_word}")
            # add every character of current word/next word to all characters set
            self.all_chs.update(list(curr_word))
            self.all_chs.update(list(next_word))
            # edge case, check if b is a prefix of a and they are not the same
            if len(curr_word) > len(next_word) and curr_word[:len(next_word)] == next_word:
                # print(f"{next_word} is a prefix of {curr_word}")
                return ""
            # for every comparable character
            for i in range(min(len(curr_word), len(next_word))):
                # print(f"Comparing {curr_word[i]} to {next_word[i]}")
                if curr_word[i] != next_word[i]:
                    # add to the adjacency list
                    self.adj_list[curr_word[i]].append(next_word[i])
                    # print(f"New adjacency list: {self.adj_list}")
                    # check for a cycle
                    if is_cycle(curr_word[i], next_word[i]):
                        # print(f"Found a cycle between {curr_word[i]} and {next_word[i]}, returning blank")
                        return ""
                    # break the checks, you don't know anything about the rest of the letters
                    break
        
        # step 2: do a topological sort
        # define a function to do the topological sort
        def topoSort(ch):
            self.visited_chs.add(ch)
            
            for neighbor in self.adj_list[ch]:
                if neighbor not in self.visited_chs:
                    topoSort(neighbor)
            
            self.stack.append(ch)
        
        # run the topological sort
        self.visited_chs = set()
        self.stack = []

        for ch in self.adj_list:
            if ch not in self.visited_chs:
                topoSort(ch)
        
        lexicography = ''.join(self.stack[::-1])
        res = ''
        for ch in lexicography:
            res += ch
            self.all_chs.remove(ch)
        remaining_chs = ''.join(list(self.all_chs))
        res += remaining_chs
        return res
