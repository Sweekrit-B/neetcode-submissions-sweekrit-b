class TrieNode():
    def __init__(self):
        self.endOfWord = False
        self.neighbors = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        curr = self.root
        for ch in word:
            if ch not in curr.neighbors:
                curr.neighbors[ch] = TrieNode()
            curr = curr.neighbors[ch]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # key idea here - the time complexity of doing a BFS search is O(V + V^2)
            # this means that to search for w words of length n, the time complexity is O(wn^2)
            # if we were to create a prefix tree of the whole grid, the time complexity is O(n^4)
        # the best method, seemingly, is to find the number of words that are not WITHIN other words
            # however, then the question becomes how do you deal with something like "cat" and "scat"
            # "cat" is technically within "scat", but prefix trie wise its hard to implement
            # however, since its not a prefix, don't really need to worry about that
        
        # strategy
            # add every word in words to a single trie
            # then, for every index in the grid
                # walk in the direction of the trie
                # if you get to a point where there is nothing else, then if that is a word, mark it down!
        
        trie = Trie()
        for word in words:
            trie.add(word)
        
        def is_valid(cell):
            i, j = cell
            if (0 <= i < len(board)) and (0 <= j < len(board[0])):
                return True
            return False

        def dfs(curr, cell, word):
            i, j = cell
            # if we have already visited
            if (i, j) in visited:
                return
            # if there are no neighbors
            if not curr.neighbors:
                return
            if board[i][j] in curr.neighbors:
                # move the value that we are looking at at the trie node forward
                curr = curr.neighbors[board[i][j]]
                # add to the word
                word += board[i][j]
                # if the new current value (i.e. a valid character) is the end of something, add that word
                if curr.endOfWord:
                    all_words.add(word)
                # find all the grid neighbors
                grid_neighbors = [
                    (i+1, j),
                    (i-1, j),
                    (i, j+1),
                    (i, j-1)
                ]
                # add to visited
                visited.add((i, j))
                # for each of the valid grid neighbors, run this dfs
                for cell in grid_neighbors:
                    if is_valid(cell):
                        dfs(curr, cell, word)
                # remove from visited
                visited.remove((i, j))
            return
        
        all_words = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                dfs(trie.root, (i, j), "")
        
        return list(all_words)
        
