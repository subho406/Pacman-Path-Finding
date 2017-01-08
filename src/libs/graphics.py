import pygame
import math
from . import vector
def animategraph(maze,m,n,pacpos,foodpos,searchdata,pathdata):
    boxsize=20
    pygame.init()
    screen = pygame.display.set_mode(((n+2)*boxsize, (m+2)*boxsize))
    done = False
    clock = pygame.time.Clock()
    finishanimation=False
    while not done:
            if finishanimation==False:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                screen.fill((0, 0, 0))
                xpos=0
                ypos=0
                for line in maze:
                    ypos=ypos+boxsize
                    xpos=0
                    for ch in line:
                        xpos=xpos+boxsize
                        if(ch=='%'):
                            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(xpos, ypos, boxsize, boxsize))
                pygame.draw.circle(screen, (255, 128, 0), (pacpos.y*boxsize+boxsize+int(boxsize/2),pacpos.x*boxsize+boxsize+int(boxsize/2)), int(boxsize/2), 0)
                pygame.draw.circle(screen, (255, 128, 128), (foodpos.y*boxsize+boxsize+int(boxsize/2),foodpos.x*boxsize+boxsize+int(boxsize/2)), int(boxsize/2), 0)
                for data in searchdata:
                    pygame.draw.circle(screen, (0, 255, 25), (data.y*boxsize+boxsize+int(boxsize/2),data.x*boxsize+boxsize+int(boxsize/2)), int(boxsize/4), 0)
                    pygame.display.flip()
                    pygame.time.wait(50)
                for i in range( 0,len(pathdata)-1):
                    pygame.draw.line(screen, (255,0,28), (pathdata[i].y*boxsize+boxsize+int(boxsize/2),pathdata[i].x*boxsize+boxsize+int(boxsize/2)), (pathdata[i+1].y*boxsize+boxsize+int(boxsize/2),pathdata[i+1].x*boxsize+boxsize+int(boxsize/2)), 4)
                    pygame.display.flip()
                    pygame.time.wait(50)
                finishanimation=True
            pygame.display.flip()
            clock.tick(60)

if __name__=='__main__':
    print('Enter graph data one by one.')
    pacpos=input().split(' ')
    pacpos=vector(int(pacpos[0]),int(pacpos[1]))
    foodpos=input().split(' ')
    foodpos=vector(int(foodpos[0]),int(foodpos[1]))
    coords=input().split(' ')
    m,n=int(coords[0]),int(coords[1])
    maze=[]
    for i in range(0,m):
        maze.append(input())
    print('Enter search followed by path found')
    n1=int(input())
    searchdata=[]
    for i in range(0,n1):
        pos=input().split(' ')
        pos=vector(int(pos[0]),int(pos[1]))
        searchdata.append(pos)
    n2=int(input())
    pathdata=[]
    for i in range(0,n2):
        pos=input().split(' ')
        pos=vector(int(pos[0]),int(pos[1]))
        pathdata.append(pos)
    animategraph(maze,m,n,pacpos,foodpos,searchdata,pathdata)


