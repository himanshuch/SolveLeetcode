class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def removeWord(self):
        cur = self
        cur.endOfWord= False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.directions = [[0,1], [1,0], [0,-1], [-1,0]]
        res = []
        #visited = set()
        m, n = len(board), len(board[0])

        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        def dfs(row, col, node, word):
            if row<0 or col<0 or row >=m or col>=n or board[row][col] not in node.children:
                return

            word += board[row][col]
            node = node.children[board[row][col]]
            if node.endOfWord:
                node.removeWord()
                res.append(word)

            tmp = board[row][col]
            board[row][col] = "#"
            #visited.add((row, col))
            for r, c in self.directions:  
                dfs(row+r, col+c, node, word)
            board[row][col] = tmp
            #visited.remove((row, col))  

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
                        
        return res               