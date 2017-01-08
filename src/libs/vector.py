'Vector of the position '
import math


class vector:
	x=None
	y=None
	parent=None
	dist=0
	cost=math.inf  #For dijkstra implementation
	def __init__(self,x,y):
	  	self.x=x
	  	self.y=y
	#If compared with other object when using heaps return true as it does not matter who is inserted first when two nodes have same cost
	def __lt__(self, other): 
		return True
	def __repr__(self):
		return "("+str(self.x)+","+str(self.y)+")\n"
	
