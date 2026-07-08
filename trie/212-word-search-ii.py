from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        ans = []

        def dfs(row: int, col: int, node: TrieNode) -> None:
            if row < 0 or row == rows or col < 0 or col == cols:
                return

            char = board[row][col]
            if char == "#" or char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                ans.append(next_node.word)
                next_node.word = None

            board[row][col] = "#"
            dfs(row + 1, col, next_node)
            dfs(row - 1, col, next_node)
            dfs(row, col + 1, next_node)
            dfs(row, col - 1, next_node)
            board[row][col] = char

            if not next_node.children and next_node.word is None:
                del node.children[char]

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    print(Solution().findWords(board, ["oath", "pea", "eat", "rain"]))
# DEBUG RUNNER END
