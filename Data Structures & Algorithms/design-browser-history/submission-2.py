class Node:
    def __init__(self, homepage: str, prev: Optional[Node] = None, next: Optional[Node] = None):
        self.prev = prev
        self.url = homepage
        self.next = next

class BrowserHistory:
    # doubly linked list system -> store the prev and the next value
    # takes more memory and around the same runtime (if visit & forward/back operations are the roughly the same)

    def __init__(self, homepage: str):
        self.currNode = Node(homepage)
        # print(f"Initialized with a root: {root.url}")

    def visit(self, url: str) -> None:
        newNode = Node(url)
        # link the new node to the current node
        newNode.prev = self.currNode
        self.currNode.next = newNode
        self.currNode = newNode
        return

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.currNode.prev:
            self.currNode = self.currNode.prev
            i += 1
        return self.currNode.url

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.currNode.next:
            self.currNode = self.currNode.next
            i += 1
        return self.currNode.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)