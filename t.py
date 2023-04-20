

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
def DFSsearch(grid):
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    visited = {startCell:None}
    stack = deque([startCell])
    while stack:
        current = stack.pop()
        
        if current in goalCells:
            while current is not None  and current is not startCell: 
                print(current)
                path.append(current)
                current = visited[current]
            path.reverse()
            grid.resetGrid()
            return path
        del visited[current]
        # for v in visited.values():
        #     print(v)
        # print()
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            
            if nextNode is None or nextNode.isWall():
                continue
            if nextNode in visited and nextNode not in stack:
                continue
            nextNode.setVisited(True)
            visited[nextNode] = current
            #print(nextNode)
            stack.append(nextNode)
    return None
# import heapq
# class Node: #node to store the cell and pirority
#         def __init__(self,cell,priority):
#             self.cell = cell
#             self.priority = priority #priority is calculated based on path cost and manhattan distance
        
#         def __lt__(self, other): #less than operator to compare between nodes
#             return self.priority < other.priority 
        
#         def __str__(self): #to print the Node
#             return f"priority: {self.priority}, cell: {self.cell}"
# lst = []
# heapq.heappush(lst, Node("a",1))
# heapq.heappush(lst, Node("b",2))
# heapq.heappush(lst, Node("c",3))
# heapq.heappush(lst, Node("d",4))
# heapq.heappush(lst, Node("e",2))
# heapq.heappush(lst, Node("f",1))
# for i in range(6):
#     print(lst[i])
# print()
# for i in range(6):
#     print(heapq.heappop(lst))
def DFSsearch(grid,draw=True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    path = []
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    moves = [(0,-1),(-1,0),(0,1),(1,0)] # up, left, down, right
    queue = [] #queue for cell
    queue.append(startCell)
    visited = {startCell: [startCell]} # visited dictionary to store the parent nodes
    node = 1
    while queue: #while queue not empty
        current = queue.pop() #pop the first element
        current.setVisited(True)
        if draw: #visualise when required
                current.setFrontier(False)
                grid.drawNode(current)
        if current in goalCells: #current is goal
            path = visited[current]
            if draw:
                return path #return the path
            else:
                return path, node
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            if nextNode is None or nextNode.isVisited() or nextNode.isWall(): #if the next node is none or already visited or a wall
                continue           
            
            visited[nextNode] = visited[current] + [nextNode] #return a list of parent nodes
            node +=1
            queue.append(nextNode)
            if draw: #visualise when required
                nextNode.setFrontier(True)
                grid.drawNode(nextNode)
    if draw:
        return None
    else:
        return None, node

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
input_row = pygame.Rect(50, 50, 300, 50)
input_column = pygame.Rect(50, 120, 300, 50)
row_text = ""
column_text = ""

# Set up the loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                row_text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                row_text = row_text[:-1]

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the input box
    pygame.draw.rect(screen, (0, 0, 0), input_row, 2)
    pygame.draw.rect(screen, (0, 0, 0), input_column, 2)
    # Draw the input text
    text_surface = font.render(row_text, True, (0, 0, 0))
    screen.blit(text_surface, (input_row.x + 5, input_row.y + 5))

    # Update the screen
    pygame.display.flip()

# Get the number from the input text
if input_text:
    number = int(input_text)
    print(f"The user entered the number: {number}")

# Quit Pygame
pygame.quit()
def CUS1search(grid, draw = True): #uninformed search is bidirectional search
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    node = 2
    while goalCells:
        forwardQueue = deque()
        forwardQueue.append(startCell)
        forwardVisited = {startCell: [startCell]} #the list is the path to the cell
        
        backwardQueue = deque()
        goalCell = goalCells.pop(1)
        backwardQueue.append(goalCell)
        backwardVisited = {goalCell: [goalCell]} #choose the first goal cell in the cell list
        
        visitedIntersection = None #the intersection cell
        
        while forwardQueue and backwardQueue: #check when both queues are empty
            forward = forwardQueue.popleft()
            if draw: #visualise when required
                forward.setFrontier(False)
                forward.setVisited(True)
                grid.drawNode(forward)
            for move in moves:
                nextNode = grid.locateCellCoord(move[0]+forward.x, move[1]+forward.y)
                if nextNode is None or nextNode.isWall() or  nextNode in forwardVisited: #check if the next node satisfy the requirement
                    continue
                
                forwardQueue.append(nextNode) #append the node into the queue
                forwardVisited[nextNode] = forwardVisited[forward] + [nextNode] #the value is the list of path to the cell
                node +=1
                if draw: #draw when required
                    nextNode.setFrontier(True)
                    grid.drawNode(nextNode)
                if nextNode in backwardVisited: #if the node is in backward
                    visitedIntersection = nextNode #find the intersection
                    break #break the loop
            if visitedIntersection is not None:
                break
            
            backward = backwardQueue.popleft()
            if draw: #visualise when required
                backward.setFrontier(False)
                backward.setVisited(True)
                grid.drawNode(backward)
            for move in moves:
                nextNode = grid.locateCellCoord(move[0]+backward.x, move[1]+backward.y)
                if nextNode is None or nextNode.isWall() or  nextNode in backwardVisited: #check if the next node satisfy the requirement
                    continue
                node += 1
                backwardQueue.append(nextNode) #append the node into the queue
                backwardVisited[nextNode] = backwardVisited[backward] + [nextNode] #the value is the list of path to the cell
                if draw: #draw when required
                    nextNode.setFrontier(True)
                    grid.drawNode(nextNode)
                if nextNode in forwardVisited: #if the node is in forward
                    visitedIntersection = nextNode #find the intersection
                    break
            if visitedIntersection is not None:
                break
            
        if visitedIntersection is not None: #if there is intersection
            path = forwardVisited[visitedIntersection] + backwardVisited[visitedIntersection][::-1] #path will the the path to intersection in forward and reverse path in backward
            if draw:
                return path
            else:
                return path, node
        else:
            if goalCells:
                if draw:
                    grid.resetGrid(True)
                else:
                     grid.resetGrid(False)
    if draw:
        return None
    else:
        return None, node


def CUS2search(grid, draw = True):
    def manhattanDistance(a,b):
        result = abs(a.x -b.x) + abs(a.y -b.y)
        return result
    def manhattanDistance1(a,goals): #heuristic function
        result = abs(a.x -goals[0].x) + abs(a.y -goals[0].y) #return the smallest distance to any of the goal cell
        for b in goals:
            temp = abs(a.x -b.x) + abs(a.y -b.y)
            if temp <result:
                result = temp
        return result
    class Node:
        def __init__(self,cell,priority,count):
            self.cell = cell
            self.priority = priority
            self.count = count
        
        def __lt__(self, other):
            if self.priority == other.priority:
                return self.count < other.count
            return self.priority < other.priority  
        
        def __str__(self):
            return f"priority: {self.priority}, cell: {self.cell}"
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    goalCells.sort(key=lambda x: manhattanDistance(x,startCell))
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    node = 2
    while goalCells:
        forwardQueue = []
        forwardNode = Node(startCell,0,1)
        heapq.heappush(forwardQueue, forwardNode)
        forwardCost = {startCell: 0}
        forwardVisited = {startCell: [startCell]}
        
        backwardQueue = []
        goalCell = goalCells.pop(0)
        backwardNode = Node(goalCell, 0,2)
        heapq.heappush(backwardQueue, backwardNode)
        backwardVisited = {goalCell: [goalCell]}
        backwardCost = {goalCell: 0}
        
        visitedIntersection = None
        
    
        while forwardQueue and backwardQueue:
            forward = heapq.heappop(forwardQueue).cell
            if draw: #visualise when required
                    forward.setFrontier(False)
                    forward.setVisited(True)
                    grid.drawNode(forward)
            for move in moves:
                nextNode = grid.locateCellCoord(move[0]+forward.x, move[1]+forward.y)
                if nextNode is None or nextNode.isWall() or  nextNode in forwardVisited:
                    continue
                
                newCost = forwardCost[forward] + 1
                
                if nextNode not in forwardCost or newCost < forwardCost[nextNode]:
                    forwardCost[nextNode] = newCost
                    priority = newCost + manhattanDistance(nextNode, goalCell)
                    node +=1
                    temp = Node(nextNode,priority, node)
                   
                    if draw: #draw when required
                        nextNode.setFrontier(True)
                        grid.drawNode(nextNode)
                    forwardVisited[nextNode] = forwardVisited[forward] + [nextNode]
                    heapq.heappush(forwardQueue, temp)
                
                if nextNode in backwardVisited:
                    visitedIntersection = nextNode
                    break
            if visitedIntersection is not None:
                break
            
            backward = heapq.heappop(backwardQueue).cell
            if draw: #visualise when required
                    backward.setFrontier(False)
                    backward.setVisited(True)
                    grid.drawNode(backward)
            for move in moves:
                nextNode = grid.locateCellCoord(move[0]+backward.x, move[1]+backward.y)
                if nextNode is None or nextNode.isWall() or  nextNode in backwardVisited:
                    continue
                            
                newCost = backwardCost[backward] + 1
                
                if nextNode not in backwardCost or newCost < backwardCost[nextNode]:
                    backwardCost[nextNode] = newCost
                    priority = newCost + manhattanDistance(nextNode, startCell)
                    node+=1
                    temp = Node(nextNode,priority, node)
                    
                    if draw:
                        nextNode.setFrontier(True)
                        grid.drawNode(nextNode)
                    backwardVisited[nextNode] = backwardVisited[backward] + [nextNode]
                    heapq.heappush(backwardQueue, temp)
                
                if nextNode in forwardVisited:
                    visitedIntersection = nextNode
                    break
            if visitedIntersection is not None:
                break
        
        if visitedIntersection is not None:
            path = forwardVisited[visitedIntersection] + backwardVisited[visitedIntersection][::-1]
            if draw:
                return path
            else:
                return path, node
        else:
            if goalCells:
                if draw:
                    grid.resetGrid(True)
                else:
                    grid.resetGrid(True)
    if draw:
        return None
    else:
        return None, node