import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while len(queue) != 0:
            word, length = queue.popleft()
            # print(f"Got {word} with {length}")
            if word == endWord:
                # print(f"{word} is {endWord}, returning {length}")
                return length
            for i in range(len(word)): # for each letter in the current word
                for c in string.ascii_lowercase: # for each possible character
                    next_word = word[:i] + c + word[i+1:] # create the next word
                    if next_word in word_set and next_word not in visited: # if all conditions are met
                        visited.add(next_word)
                        queue.append((next_word, length + 1))
        
        return 0