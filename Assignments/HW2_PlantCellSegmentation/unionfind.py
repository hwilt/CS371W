class UnionFindOpt():
	def __init__(self, n):
		self.n = n
		self.normal = [i for i in range(n)]
		self._parent = [i for i in range(n)]
		self._weights = [1 for i in range(n)]

	def root(self, i):
		if i != self.parent[i]:
			self._operations += 1
			parent[i] = root(parent[i])
		return parent[i]

	def find(self, i, j):
		return self.root(i) == self.root(j)

	def union(self, i, j):
		root_i = self.root(i)
		root_j = self.root(j)
		if root_i != root_j: #if not in the same root/ group
			if self._weights[root_j] >= self._weights[root_i]:
				self._weights[root_j] += self._weights[root_i]
				self._weights[root_i] = 0
				self._parent[root_i] = j
			else:
				self._weights[root_i] += self._weights[root_j]
				self._weights[root_j] = 0
				self._parent[root_j] = i

	def __str__(self):
		return 'Normal: ' + str(self.normal) + '\nParents:' + str(self._parent) + '\nWeights:' + str(self._weights)