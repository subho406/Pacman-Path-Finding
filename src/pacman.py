
class vector:
	x=None
	y=None
	parent=None
	dist=0
	def __init__(self,x,y):
	  	self.x=x
	  	self.y=y


def reconstructpath(nodelist,goalindex):
	path=[]
	while(nodelist[goalindex].parent!=None):
		path.append(nodelist[goalindex])
		goalindex=nodelist[goalindex].parent
	path.append(nodelist[goalindex])
	return path

def movegen(matrix,pos,m,n):
	neighbours=[]
	if(pos.x!=0 and matrix[pos.x-1][pos.y]!='%'):
		neighbours.append(vector(pos.x-1,pos.y))
	if(pos.y!=0 and matrix[pos.x][pos.y-1]!='%'):
		neighbours.append(vector(pos.x,pos.y-1))
	if(pos.y+1!=n and matrix[pos.x][pos.y+1]!='%'):
		neighbours.append(vector(pos.x,pos.y+1))
	if(pos.x+1!=m and matrix[pos.x+1][pos.y]!='%'):
		neighbours.append(vector(pos.x+1,pos.y))
	return neighbours 

def inclosed(closed,node):
	for a in closed:
		if (a.x==node.x and a.y==node.y):
			return False
	return True

def goaltest(node,goal):
	if(node.x==goal.x and node.y==goal.y):
		return True
	else:
		return False
def dfs(matrix,start,goal,m,n):
	open=[]
	closed=[]
	open.append(start)	
	while (len(open)!=0):
		node=open.pop()
		closed.append(node)
		if(goaltest(node,goal)):
			return closed
		neighbours = movegen(matrix,node,m,n)
		for x in neighbours:
			if inclosed(closed,x):
				x.parent=len(closed)-1
				x.dist=node.dist+1
				open.append(x)				
	return False


if __name__ == '__main__':
	pacpos=input().split(' ')
	pacpos=vector(int(pacpos[0]),int(pacpos[1]))
	foodpos=input().split(' ')
	foodpos=vector(int(foodpos[0]),int(foodpos[1]))
	coords=input().split(' ')
	m,n=int(coords[0]),int(coords[1])
	maze=[]
	for i in range(0,m):
		maze.append(input())
	val=dfs(maze,pacpos,foodpos,m,n)
	print(len(val))
	for x in val:
		print(str(x.x)+' '+str(x.y))
	print(val[len(val)-1].dist) # print the dist to the last node ie goal node
	path=reconstructpath(val,len(val)-1)
	for i in range(len(path)-1,-1,-1):
		print(str(path[i].x)+' '+str(path[i].y))
