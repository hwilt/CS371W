class UnionFindOpt():
	def __init__(self, n):
		self.n = n
		self.normal = [i for i in range(n)]
		self._parent = [i for i in range(n)]
		self._weights = [1 for i in range(n)]
		#self._operations = 0
		#self._calls = 0

	def root(self, i):
		rootnot_lowest = []
		while i != self._parent[i]:
			#self._operations += 1
			rootnot_lowest.append(i)
			i = self._parent[i]
		if rootnot_lowest:
			for j in rootnot_lowest:
				self._parent[j] = i
		return i

	def find(self, i, j):
		#self._calls += 1
		return self.root(i) == self.root(j)

	def union(self, i, j):
		#self._calls += 1
		root_i = self.root(i)
		root_j = self.root(j)
		if root_i != root_j: #if not in the same root/ group
			if self._weights[root_j] >= self._weights[root_i]:
				#self._operations += 1
				self._weights[root_j] += self._weights[root_i]
				self._weights[root_i] = 0
				self._parent[root_i] = j
			else:
				#self._operations += 1
				self._weights[root_i] += self._weights[root_j]
				self._weights[root_j] = 0
				self._parent[root_j] = i
			#self._parent[root_j] = i
			#self._weights[root_j] += self._weights[root_i]
			#self._weights[root_j] = 0

	def __str__(self):
		return 'Normal: ' + str(self.normal) + '\nParents:' + str(self._parent) + '\nWeights:' + str(self._weights)

def main():
	x = UnionFindOpt(10)
	string = "Start:\n" + str(x)
	print(string)
	x.union(0,2)
	x.union(1,8)
	x.union(7,8)
	x.union(1,6)
	x.union(0,1)
	x.union(6,9)
	x.union(9,5)
	x.union(3,4)
	x.union(4,1)
	string = "End:\n" + str(x)
	print(string)

if __name__ == "__main__":
	main()