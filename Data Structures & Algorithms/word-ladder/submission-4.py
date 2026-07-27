import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # word_set = set(wordList)
        one_letter_away_map = defaultdict(list)

        def one_letter_diff(w1, w2):
            mismatches = sum(c1 != c2 for c1, c2 in zip(w1, w2))
            return mismatches == 1
        
        for w1 in wordList + [beginWord, endWord]:
            one_letter_away_map[w1] = [w2 for w2 in wordList if one_letter_diff(w1, w2)]
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while len(queue) != 0:
            word, length = queue.popleft()
            # print(f"Got {word} with {length}")
            if word == endWord:
                # print(f"{word} is {endWord}, returning {length}")
                return length
            for next_word in one_letter_away_map[word]:
                if next_word not in visited: # if we have not already seen this
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
        
        return 0