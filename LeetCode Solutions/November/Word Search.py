"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		wordEncd = Counter(word)
		m, n = len(board), len(board[0])
		dic = defaultdict(set)

		for i in range(m):
			for j in range(n):
				if board[i][j] in wordEncd:
					dic[board[i][j]].add((i, j))

		if len(wordEncd) != len(dic):
			return False

		for ch, count in wordEncd.items():
			if len(dic[ch]) < count:
				return False

		if len(dic[word[-1]]) < len(dic[word[0]]):
			word = word[::-1]

		length = len(word)
		def dfs(cord, indx):
			if indx == length:
				return True
			ch = word[indx]
			i, j = cord
			for cand in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
				if cand in dic[ch]:
					dic[ch].remove(cand)
					if dfs(cand, indx + 1):  return True
					dic[ch].add(cand)
			return False

		for cord in list(dic[word[0]]):
			dic[word[0]].remove(cord)
			if dfs(cord, 1): return True
			dic[word[0]].add(cord)

		return False