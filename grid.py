from cell import Cell
import pygame
class Grid:
    def __init__(self,rows,cols):
        self.cols = cols #number of rows
        self.rows = rows #number of columns
        self.grid = []
        self.screen = None
        self.createCells()
        
    def AddCell(self,cell): #add new cell to the grid
        self.grid.push(cell)
        
    def locateCell(self,row,col): #locate cell based on row and column
        for cell in self.grid:
            if cell.x == col and cell.y == row:
                return cell
        return None
    
    def locateCellCoord(self,x,y): #locate cell based ont he coord
        for cell in self.grid:
            if cell.x == x and cell.y == y:
                return cell
        return None
    
    def locateGoalCells(self): #locate the goal cells
        result = []
        for cell in self.grid:
            if cell.isGoal():
                result.append(cell)
        return result
    
    def locateStartCell(self): #locate the start cell
        for cell in self.grid:
            if cell.isStart():
                return cell
        return None
    
    def setStartCell(self,x,y): #set start cell with the coordinate
        cell = self.locateCellCoord(x,y)
        cell.setStart(True)
    
    def setWallCells(self,lst): #set wall cell
        for x in range(lst[2]):
            for y in range(lst[3]):
                cell = self.locateCell(lst[1]+y,lst[0]+x)
                cell.setWall(True)
            
            
    def setGoalCells(self,lst):
        for coord in lst:
            cell = self.locateCell(coord[1], coord[0])
            cell.setGoal(True)
        
    def resetGrid(self, draw = True): #reset all visited state of the cells
        for cell in self.grid:
            cell.reset()
        if draw:
            self.draw()
    def createCells(self):
        for x in range(self.cols):
            for y in range(self.rows):
                self.grid.append(Cell(x,y))
                
    def setScreen(self,screen):
        self.screen = screen
                
    def draw(self):
        for cell in self.grid:
            cell.draw(self.screen)
                    
    def drawNode(self,node): #draw a specific cell on the gui
        node.draw(self.screen)
        pygame.time.delay(35)
        pygame.display.update()
                