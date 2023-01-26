from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = {}

    def addWord(self, word):
        for c in word:
            if c not in self.children:
                self.children[c] = Trie()
            self = self.children[c]
        self.isWord = True

    @staticmethod
    def prune(word, root):
        trie = root
        stack = []

        for c in word:
            stack.append(trie)
            trie = trie.children[c]
        trie.isWord = False

        for t_node, c in reversed(list(zip(stack, word))):
            if len(t_node.children[c].children) > 0:  # has children
                return
            else:
                del t_node.children[c]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited = set(), set()
        rows, cols = len(board), len(board[0])
        trieNode = Trie()
        root = trieNode
        for word in words:
            trieNode.addWord(word)

        def dfs(row, col, node, word):
            if (row < 0 or col < 0 or row == rows or col == cols or
                    (row, col) in visited or
                    board[row][col] not in node.children):
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isWord:
                res.add(word)
                node.prune(word, root)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            visited.remove((row, col))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trieNode, "")

        return list(res)
