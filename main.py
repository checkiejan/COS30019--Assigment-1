import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hide welcome prompt from pygame
from cell import Cell
from grid import Grid
from button import Button
import pygame
from algo import *
import sys
screen_width = 800
screen_height = 800
W,H = 0,0
goals = []
start = 0 
grid = 0
def getGoal(lst): #set goal cells in the grid
    result = []
    for x in lst:
        result.append(list(map(int,x.strip().strip("(\n)").split(","))))
    return result #return a list of postions of goal cells
        
def getWH(lst): #set number of rows and columns for the grid
    global W, H  
    W, H= list(map(int,lst.split(','))) #split it by commma then map the values into W and H
    
def createButtons(lst):
        y = 500
        width = 70
        height = 40
        padding = 30
        x = (screen_width - (width +padding)*3)/2
        bfs = Button(x,y,width,height,"BFS")
        bfs.setSearch(BFSsearch)
        lst.append(bfs)
        x+= width + padding
        dfs = Button(x,y,width,height,"DFS")
        dfs.setSearch(DFSsearch)
        lst.append(dfs)
        x+= width + padding
        AS = Button(x,y,width,height,"A*")
        AS.setSearch(ASsearch)
        lst.append(AS)
        x =(screen_width - (width +padding)*3)/2
        y += height + padding
        gbfs =  Button(x,y,width,height,"GBFS")
        gbfs.setSearch(GBFSsearch)
        lst.append(gbfs)
        x+= width + padding
        cus1 = Button(x,y,width,height,"CUS1")
        cus1.setSearch(CUS1search)
        lst.append(cus1)
        x+= width + padding
        cus2 = Button(x,y,width,height,"CUS2")
        cus2.setSearch(CUS2search)
        lst.append(cus2)
      
with open(sys.argv[1],"r") as f: 
    lst = f.readline().strip("[\n]") # get rip of \n character
    getWH(lst) #get width, height of the map
    grid = Grid(W,H)
    lst = f.readline().strip("(\n)")
    x,y = list(map(int,lst.split(','))) #get position of the start cell
    grid.setStartCell(x,y)
    lst = f.readline().strip("\n") #get position of the goal cells
    lst = lst.split("|")
    lst = getGoal(lst) #set goal cells
    grid.setGoalCells(lst)
    
    for line in f: #loop til the end of the file
        lst= list(map(int,line.strip("(\n)").split(","))) # get position of the wall cells
        grid.setWallCells(lst) 
        
methods = ["bfs",'dfs',"as","gbfs","cus1","cus2","dfsr"]
if len(sys.argv) == 3:
    method = sys.argv[2].lower()
    
    if method in methods:
        t = None
        if method == "bfs":
            t,node = BFSsearch(grid,False)
        elif method == "dfs":
            t,node = DFSsearch(grid,False)
        elif method == "as":
            t,node = ASsearch(grid,False)
        elif method == "dfsr":
            t,node = DFSRecursivesearch(grid,False)
        elif method == "gbfs":
            t,node = GBFSsearch(grid,False)
        elif method == "cus1":
            t,node = CUS1search(grid,False)
        elif method == "cus2":
            t,node = CUS2search(grid,False)
        print(f'{sys.argv[1]} {method} {node}')
        print(encodePath(t))
    else:
        print("Unknown method")
elif len(sys.argv) > 2:
    print("wrong number of argument")
else:
    buttons = []
    createButtons(buttons)
    pygame.init()
    t = None
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Maze')
    running = True
    grid.setScreen(screen)
    search = False
    drawPath = False
    path = None
    strategy = None
    name = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    search = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button.onPoint(pygame.mouse.get_pos()):
                        grid.resetGrid()
                        search = True
                        strategy = button.search()
                        name = button.text.lower()
                        break
        screen.fill((255, 255, 255))
        grid.draw()
        if search and strategy is not None:
            path,node = strategy(grid)
            print(f'{sys.argv[1]} {name} {node}')
            print(encodePath(path))
            search = False
            drawPath = True
        if drawPath and path is not None:
            for cell in path:
                cell.setOnPath(True)
                grid.drawNode(cell)
            drawPath = False
        
        for button in buttons:
            button.draw(screen)
        # Update the display
        
        pygame.display.update()
    pass
        

