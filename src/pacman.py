from libs import algos
from libs import vector
from libs import graphics




if __name__ == '__main__':
	#Get the Pac position,maze data and dimensions
	pacpos=input().split(' ')
	pacpos=vector.vector(int(pacpos[0]),int(pacpos[1]))
	foodpos=input().split(' ')
	foodpos=vector.vector(int(foodpos[0]),int(foodpos[1]))
	coords=input().split(' ') #Size of the data
	m,n=int(coords[0]),int(coords[1])
	maze=[]
	for i in range(0,m):
		maze.append(input())  #Add maze data one by one
	path,search=algos.dijkstraunweighted(maze,pacpos,foodpos,m,n)
	graphics.animategraph(maze,m,n,pacpos,foodpos,search,path)
