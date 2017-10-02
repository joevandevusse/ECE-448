class my_node:
	def __init__(self):
		self.edges = []  #these are the neighbors
		self.goals = []
		self.goal = False 
		self.start = False
		self.fscore = 0  #f(n) = g(n) + h(n)
		self.gscore = 0  #g(n)
		self.hscore = 0  #h(n)
		self.parent = None
		self.x = 0
		self.y = 0

	def __iter__(self):
	    return self

	def __str__(self):
		return str((self.x,self.y))

	def __hash__(self):
		return hash((self.x,self.y))

	def __eq__(self,other):
		return (self.x,self.y)==(other.x,other.y)

	def __lt__(self, other):
		return (self.fscore < other.fscore)

	def __gt__(self, other):
		return (self.fscore > other.fscore)
      
	def get_neighbors(self, id):
		return self.edges[id]

	def set_neighbors(self, neighor):
		self.edges.append(neighbor)

	def set_goals(self, goal):
	    self.goals.append(goal)

	def get_goals(self):
		return self.goals
		
	def get_parent(self):
		return self.parent
		
	def get_fscore(self):
		return self.fscore
		
	def set_parent(self,parent):
		self.parent = parent
		
	def set_fscore(self,fscore):
		self.fscore = fscore

	__repr__ = __str__

