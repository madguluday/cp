#heap sort
def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1 
	r = 2 * i + 2 
	if l < n and arr[i] < arr[l]:
		largest = l
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])
		heapify(arr, n, largest)
def heapSort(arr):
	n = len(arr)
	for i in range(n // 2, -1, -1):
		heapify(arr, n, i)
	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)
arr = [2,9,7,6,5,8]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
	print(arr[i])
	
#breadth first search


'''from collections import defaultdict 

class Graph: 
	def __init__(self): 
		self.graph = defaultdict(list) 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 
		self.visited=[] 
	def BFS(self, s): 
		queue = [] 
		queue.append(s) 
		self.visited.append(s) 

		while queue: 

			s = queue.pop(0) 
			print (s, end = " ") 
			for i in self.graph[s]: 
				if i not in visited: 
					queue.append(i) 
					self.visited.append(s) 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)") 
#g.BFS(0) '''
