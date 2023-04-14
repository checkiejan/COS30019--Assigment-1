import pygame
class Cell:
    def __init__(self, x,y ):
        self.x = x
        self.y = y
        self.goal = False
        self.wall = False
        self.start = False
        self.visited = False
        self.onPath = False
        self.width = 40
        self.row = self.width * self.x +20
        self.column = self.width * self.y +20
        self.padding = 2
        
    def setWall(self,value):
        self.wall = value
    
    def setGoal(self,value):
        self.goal = value
    
    def setStart(self,value):
        self.start = value
        
    def setVisited(self,value):
        self.visited = value
        
    def setOnPath(self,value):
        self.onPath = value
        
    def isStart(self):
        return self.start
    
    def isWall(self):
        return self.wall
        
    def isGoal(self):
        return self.goal 
    
    def isVisited(self):
        return self.visited
    
    def isOnPath(self):
        return self.onPath
    
    def reset(self):
        self.visited = False
        self.onPath = False
        
    def __str__(self):
        return f'row: {self.y}, col: {self.x}, goal: {self.goal}, wall: {self.wall}, start: {self.start}'
    
    def draw(self,screen):
        pygame.draw.rect(screen, (0,0,0), (self.row, self.column, self.width, self.width))
        if self.isWall():
            pygame.draw.rect(screen, (69,69,69), (self.row + self.padding, self.column + self.padding, self.width - self.padding*2, self.width- self.padding*2))
            return
            
            
        if self.isGoal():
            pygame.draw.rect(screen, (221, 255, 187), (self.row + self.padding, self.column + self.padding, self.width - self.padding*2, self.width- self.padding*2))
            return
        
        if self.isStart():
            pygame.draw.rect(screen, (241, 90, 89), (self.row + self.padding, self.column + self.padding, self.width - self.padding*2, self.width- self.padding*2))
            return
        if self.isOnPath():
            pygame.draw.rect(screen, (255, 241, 220), (self.row + self.padding, self.column + self.padding, self.width - self.padding*2, self.width- self.padding*2))
            return
        
        if self.isVisited():
           # pygame.draw.rect(screen, (216, 216, 216), (self.row + self.padding, self.column + self.padding, self.width - self.padding*2, self.width- self.padding*2))
            pygame.draw.rect(screen, (135, 203, 185), (self.row + self.padding, self.column + self.padding, self.width - self.padding*2, self.width- self.padding*2))

            return

        
        
        pygame.draw.rect(screen, (255,255,255), (self.row + self.padding, self.column + self.padding, self.width - self.padding*2, self.width- self.padding*2))
       
    