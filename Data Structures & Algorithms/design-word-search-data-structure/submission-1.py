class TreeNode:

    def __init__(self, end: Optional[bool] = False):
        self.end = end
        self.neighbors = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.neighbors:
                curr.neighbors[ch] = TreeNode()
            curr = curr.neighbors[ch]
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(ix, curr):
            if ix == len(word):
                return curr.end == True

            if word[ix] == ".":
                for neighbor in curr.neighbors.values(): # for all neighboring nodes
                    if dfs(ix+1, neighbor):
                        return True # check if the dfs works fine
                return False
            else:
                if word[ix] not in curr.neighbors:
                    return False # there is no next point
                next_node = curr.neighbors[word[ix]]
                return dfs(ix+1, next_node)
            
        return dfs(0, self.root)