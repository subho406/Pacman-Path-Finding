'''
Module algos
Contains the following AI Algorithms

'''
from . import vector
import heapq


def inclosed(closed,node):
	for a in closed:
		if (a.x==node.x and a.y==node.y):
			return True
	return False

def goaltest(node,goal):
	if(node.x==goal.x and node.y==goal.y):
		return True
	else:
		return False
		
def movegen(matrix,pos,m,n):
	neighbours=[]
	if(pos.x!=0 and matrix[pos.x-1][pos.y]!='%'):
		neighbours.append(vector.vector(pos.x-1,pos.y))
	if(pos.y!=0 and matrix[pos.x][pos.y-1]!='%'):
		neighbours.append(vector.vector(pos.x,pos.y-1))
	if(pos.y+1!=n and matrix[pos.x][pos.y+1]!='%'):
		neighbours.append(vector.vector(pos.x,pos.y+1))
	if(pos.x+1!=m and matrix[pos.x+1][pos.y]!='%'):
		neighbours.append(vector.vector(pos.x+1,pos.y))
	return neighbours 
def reconstructpath(nodelist,goalindex):
	path=[]
	while(nodelist[goalindex].parent!=None):
		path.append(nodelist[goalindex])
		goalindex=nodelist[goalindex].parent
	path.append(nodelist[goalindex])
	path.reverse()
	return path

def dfs(matrix,start,goal,m,n):  #Runs DFS on a matrix, if goal is found returns the closed list(Last element is the goal node.vector of the goal else returns false
	open=[]
	closed=[]
	open.append(start)	
	while (len(open)!=0):
		node=open.pop()
		closed.append(node)
		if(goaltest(node,goal)):
			return reconstructpath(closed,len(closed)-1) ,closed
		neighbours = movegen(matrix,node,m,n)
		for x in neighbours:
			if inclosed(closed,x)==False:
				x.parent=len(closed)-1
				x.dist=node.dist+1
				open.append(x)				
	return False



def dijkstraunweighted(matrix,start,goal,m,n):  #Dijkstra implementation for array of nodes using pointersw
	openlist=[]
	closed=[]
	start.d=0
	start.cost=0
	openlist.append((0,start))
	while len(openlist)>0:
		cost,node=heapq.heappop(openlist)
		closed.append(node)
		if(goaltest(node,goal)):
			return (reconstructpath(closed,len(closed)-1), closed)
		neighbours=movegen(matrix,node,m,n)
		for x in neighbours:
			if  inclosed(closed,x)==False and (cost+1)<x.cost:
				x.dist=cost+1
				x.cost=cost+1
				x.parent=len(closed)-1
				heapq.heappush(openlist,(int(x.dist),x))
			