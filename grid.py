from cell import Cell
import pygame
class Grid:
    def __init__(self,rows,cols):
        self.cols = cols
        self.rows = rows
        self.grid = []
        self.screen = None
        self.createCells()
        
    def AddCell(self,cell):
        self.grid.push(cell)
        
    def locateCell(self,row,col):
        for cell in self.grid:
            if cell.x == col and cell.y == row:
                return cell
        return None
    
    def locateCellCoord(self,x,y):
        for cell in self.grid:
            if cell.x == x and cell.y == y:
                return cell
        return None
    
    def locateGoalCells(self):
        result = []
        for cell in self.grid:
            if cell.isGoal():
                result.append(cell)
        return result
    
    def locateStartCell(self):
        for cell in self.grid:
            if cell.isStart():
                return cell
        return None
    
    def setStartCell(self,x,y):
        cell = self.locateCellCoord(x,y)
        cell.setStart(True)
    
    def setWallCells(self,lst):
        for x in range(lst[2]):
            for y in range(lst[3]):
                cell = self.locateCell(lst[1]+y,lst[0]+x)
                cell.setWall(True)
            
            
    def setGoalCells(self,lst):
        for coord in lst:
            cell = self.locateCell(coord[1], coord[0])
            cell.setGoal(True)
        
    def resetGrid(self):
        for cell in self.grid:
            cell.reset()
            
    def createCells(self):
        for x in range(self.cols):
            for y in range(self.rows):
                self.grid.append(Cell(x,y))
                
    def setScreen(self,screen):
        self.screen = screen
                
    def draw(self):
        for cell in self.grid:
            cell.draw(self.screen)
            
    def drawSearch(self,func):
        func(self)
        
    def drawNode(self,node):
        node.draw(self.screen)
        pygame.time.delay(65)
        pygame.display.update()
                
            
            
        
    
            
    
        
    