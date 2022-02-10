class UnionFindOpt():
	def __init__(self, n):
		self.n = n
		self._parent = [i for i in range(n)]
		#self._weights = [1 for i in range(n)]

	def root(self, i):
		while i != self._parent[i]:
			i = self._parent[i]
		return i

	def find(self, i, j):
		return self.root(i) == self.root(j)

	def union(self, i, j):
		root_i = self.root(i)
		root_j = self.root(j)
		if root_i != root_j: #if not in the same root/ group
			self._parent[root_j] = root_i
			#self._weights[root_j] += self._weights[root_i]
			#self._weights[root_j] = 0

	def __str__(self):
		return str(self._parent)# + '\n' + str(self._weights)

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
	x.union(5,9)
	string = "End:\n" + str(x)
	print(string)

if __name__ == "__main__":
	main()