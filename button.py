import pygame
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 10)
my_font = pygame.font.Font(None, 30)
class Button:
    def __init__(self,x,y,width,height,text):
        self.x =x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.padding = 3
        self.text_surface = my_font.render(self.text, True, (0, 0, 0))
        self.func = None
        
    def search(self):
        return self.func
    
    def setSearch(self,func):
        self.func = func
        
    def onPoint(self,coord):
        if coord[0]>= self.x and coord[0] <= self.x + self.width and coord[1] >= self.y and coord[1] <self.y +self.height:
            return True
        return False
    def draw(self,screen):
        pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255,255,255), (self.x + self.padding, self.y+ self.padding, self.width - self.padding*2, self.height- self.padding*2))
        text_width = self.text_surface.get_width()
        text_height = self.text_surface.get_height()
        x = (self.width - text_width)/2 + self.x
        y = (self.height - text_height)/2 + self.y
        
        screen.blit(self.text_surface, (x, y))
    