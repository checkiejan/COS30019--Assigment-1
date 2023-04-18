

# def BFSsearch(grid):
#     startCell = grid.locateStartCell()
#     path = []
#     goalCells = grid.locateGoalCells()
#     moves = [(0,-1),(-1,0),(0,1),(1,0)]
#     visited = {startCell:None}
#     queue = deque([startCell])
#     while queue:
#         current = queue.popleft()
#         if current in goalCells:
#             while current is not None : 
#                 path.append(current)
#                 if current.isStart():
#                     break
#                 current = visited[current]
#             path.reverse()
#             return path
        
#         for move in moves:
#             nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            
#             if nextNode is None or nextNode.isVisited() or nextNode.isWall():
#                 continue
            
#             nextNode.setVisited(True)
#             visited[nextNode] = current
#             queue.append(nextNode)
#             grid.drawNode(nextNode)
            
#     return None
# def DFSsearch(grid):
#     startCell = grid.locateStartCell()
#     path = []
#     goalCells = grid.locateGoalCells()
#     moves = [(0,-1),(-1,0),(0,1),(1,0)]
#     visited = {startCell:None}
#     stack = deque([startCell])
#     while stack:
#         current = stack.pop()
        
#         if current in goalCells:
#             while current is not None  and current is not startCell: 
#                 print(current)
#                 path.append(current)
#                 current = visited[current]
#             path.reverse()
#             grid.resetGrid()
#             return path
#         del visited[current]
#         # for v in visited.values():
#         #     print(v)
#         # print()
#         for move in moves:
#             nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            
#             if nextNode is None or nextNode.isWall():
#                 continue
#             if nextNode in visited and nextNode not in stack:
#                 continue
#             nextNode.setVisited(True)
#             visited[nextNode] = current
#             #print(nextNode)
#             stack.append(nextNode)
#     return None
import heapq
class Node: #node to store the cell and pirority
        def __init__(self,cell,priority):
            self.cell = cell
            self.priority = priority #priority is calculated based on path cost and manhattan distance
        
        def __lt__(self, other): #less than operator to compare between nodes
            return self.priority < other.priority 
        
        def __str__(self): #to print the Node
            return f"priority: {self.priority}, cell: {self.cell}"
lst = []
heapq.heappush(lst, Node("a",1))
heapq.heappush(lst, Node("b",2))
heapq.heappush(lst, Node("c",3))
heapq.heappush(lst, Node("d",4))
heapq.heappush(lst, Node("e",2))
heapq.heappush(lst, Node("f",1))
for i in range(6):
    print(lst[i])
print()
for i in range(6):
    print(heapq.heappop(lst))
import pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Number Input")

# Set up the font
font = pygame.font.SysFont(None, 48)

# Set up the input box
input_box = pygame.Rect(50, 50, 300, 50)
input_text = ""

# Set up the loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                input_text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the input box
    pygame.draw.rect(screen, (0, 0, 0), input_box, 2)

    # Draw the input text
    text_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Update the screen
    pygame.display.flip()

# Get the number from the input text
if input_text:
    number = int(input_text)
    print(f"The user entered the number: {number}")

# Quit Pygame
pygame.quit()