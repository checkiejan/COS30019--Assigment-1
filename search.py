from grid import Grid
from collections import deque
import heapq

def BFSsearch(grid,draw=True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    path = []
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    moves = [(0,-1),(-1,0),(0,1),(1,0)] # up, left, down, right
    queue = deque() #queue for cell
    queue.append(startCell)
    visited = {startCell: [startCell]} # visited dictionary to store the parent nodes
    while queue: #while queue not empty
        current = queue.popleft() #pop the first element
        if current in goalCells: #current is goal
            path = visited[current]
            return path #return the path
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            if nextNode is None or nextNode in visited or nextNode.isWall(): #if the next node is none or already visited or a wall
                continue           
            
            visited[nextNode] = visited[current] + [nextNode] #return a list of parent nodes
            queue.append(nextNode)
            if draw: #visualise when required
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
            
    return None


def DFSsearch(grid, draw= True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    #recursive function will return the path list in correct order
    def dfs(cur, visited): #recursive function, visited is the list of visited nodes
        if cur in goalCells:
            return [cur]
        moves = [[0, -1], [-1, 0], [0, 1], [1, 0]] # up, left, down, right
        for i, j in moves:
            nextNode = grid.locateCellCoord(i+cur.x, j+cur.y) #locate the next node

            if nextNode is None or nextNode.isWall() or nextNode in visited: #if the node is none or it is wall or visited
                continue


            visited.add(nextNode) #append the node into visited list
            if draw: #draw when required
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
            res = dfs(nextNode, visited) # call the function it self
            visited.remove(nextNode) #delete them from the visited list
            if res: # if there is a way then append
                return [cur] + res

        return [] #return none when there is no way
    return dfs(startCell, {startCell})

def ASsearch(grid, draw = True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]] #up, left, down, right
    def manhattanDistance(a,goals): #heuristic function
        result = abs(a.x -goals[0].x) + abs(a.y -goals[0].y) #return the smallest distance to any of the goal cell
        for b in goals:
            temp = abs(a.x -b.x) + abs(a.y -b.y)
            if temp <result:
                result = temp
        return result
    class Node: #node to store the cell and pirority
        def __init__(self,cell,priority):
            self.cell = cell
            self.priority = priority #priority is calculated based on path cost and manhattan distance
        
        def __lt__(self, other): #less than operator to compare between nodes
            return self.priority < other.priority 
        
        def __str__(self): #to print the Node
            return f"priority: {self.priority}, cell: {self.cell}"
        
    path = [] # the path list
    visited = {startCell:None} #hash map to store parent node to trace back
    cost = {startCell: 0} #the current cost to reach to the node
    queue = []
    startCell = Node(startCell,0) 
    heapq.heappush(queue, startCell) #priority queue
    while queue:
        current = heapq.heappop(queue) #pop the first node from the queue with smallest value
        current = current.cell
        if current in goalCells: #current is goal cell
            while current is not None : #trace back from goal cell up until start cell with visited list
                path.append(current) 
                if current.isStart():
                    break
                current = visited[current]
            path.reverse() #reverse the list to make it in correct order
            return path
        
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            if nextNode is None or nextNode in visited or nextNode.isWall(): #skip if the cell does not satisfy
                continue
            new_cost = cost[current] + 1 #each cell will cost 1 to travel
            # Check if the neighbor has not been visited or the new cost is lower
            if nextNode not in cost or new_cost < cost[nextNode]: 
                cost[nextNode] = new_cost # Update the cost and add the neighbor to the priority queue
                priority = new_cost + manhattanDistance(nextNode, goalCells)
                temp = Node(nextNode,priority)
                heapq.heappush(queue, temp)
                if draw:
                    nextNode.setVisited(True)
                    grid.drawNode(nextNode)
                visited[nextNode] = current
    return None

def GBFSsearch(grid, draw = True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]] #up, left, down, right
    def manhattanDistance(a,goals): #heuristic function
        result = abs(a.x -goals[0].x) + abs(a.y -goals[0].y) #return the smallest distance to any of the goal cell
        for b in goals:
            temp = abs(a.x -b.x) + abs(a.y -b.y)
            if temp <result:
                result = temp
        return result
    class Node: #node to store the cell and pirority
        def __init__(self,cell,priority):
            self.cell = cell
            self.priority = priority #priority is calculated based manhattan distance
        
        def __lt__(self, other): #less than operator to compare between nodes
            return self.priority < other.priority 
        
        def __str__(self): #to print the Node
            return f"priority: {self.priority}, cell: {self.cell}"
        
    path = [] #the path list
    visited = {startCell:None} #hash map to store parent node to trace back
    queue = []
    startCell = Node(startCell,0) #form a node priority of zero
    heapq.heappush(queue, startCell) #priority queue to push node into queue based on the value
    while queue:
        current = heapq.heappop(queue)
        current = current.cell
        if current in goalCells: #current is goal cell
            while current is not None : #trace back from goal cell up until start cell with visited list
                path.append(current) 
                if current.isStart():
                    break
                current = visited[current]
            path.reverse() #reverse the list to make it in correct order
            return path
        
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y) #locate the cell from the grid
            if nextNode is None or nextNode.isVisited() or nextNode.isWall(): #check if the cell satisfy the requirement
                continue
            
            if nextNode not in visited: #if the node has not been visisted
                priority = manhattanDistance(nextNode, goalCells)
                temp = Node(nextNode,priority) #make a node with priority of manhattan distance
                heapq.heappush(queue, temp) #heap push the cell based on the value
                if draw: #draw when required
                    nextNode.setVisited(True)
                    grid.drawNode(nextNode)
                visited[nextNode] = current
    return None

def CUS1search(grid, draw = True): #uninformed search is bidirectional search
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    
    forwardQueue = deque()
    forwardQueue.append(startCell)
    forwardVisited = {startCell: [startCell]} #the list is the path to the cell
    
    backwardQueue = deque()
    backwardQueue.append(goalCells[0])
    backwardVisited = {goalCells[0]: [goalCells[0]]} #choose the first goal cell in the cell list
    
    visitedIntersection = None #the intersection cell
    
    while forwardQueue and backwardQueue: #check when both queues are empty
        forward = forwardQueue.popleft()
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+forward.x, move[1]+forward.y)
            if nextNode is None or nextNode.isWall() or  nextNode in forwardVisited: #check if the next node satisfy the requirement
                continue
            
            forwardQueue.append(nextNode) #append the node into the queue
            forwardVisited[nextNode] = forwardVisited[forward] + [nextNode] #the value is the list of path to the cell
            if draw: #draw when required
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
            if nextNode in backwardVisited: #if the node is in backward
                visitedIntersection = nextNode #find the intersection
                break #break the loop
        if visitedIntersection is not None:
            break
        
        backward = backwardQueue.popleft()
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+backward.x, move[1]+backward.y)
            if nextNode is None or nextNode.isWall() or  nextNode in backwardVisited: #check if the next node satisfy the requirement
                continue
            
            backwardQueue.append(nextNode) #append the node into the queue
            backwardVisited[nextNode] = backwardVisited[backward] + [nextNode] #the value is the list of path to the cell
            if draw: #draw when required
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
            if nextNode in forwardVisited: #if the node is in forward
                visitedIntersection = nextNode #find the intersection
                break
        if visitedIntersection is not None:
            break
        
    if visitedIntersection is not None: #if there is intersection
        path = forwardVisited[visitedIntersection] + backwardVisited[visitedIntersection][::-1] #path will the the path to intersection in forward and reverse path in backward
        return path
    else:
        return None

def CUS2search(grid, draw = True):
    class Node:
        def __init__(self,cell,priority):
            self.cell = cell
            self.priority = priority
        
        def __lt__(self, other):
            return self.priority < other.priority 
        
        def __str__(self):
            return f"priority: {self.priority}, cell: {self.cell}"
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    
    forwardQueue = []
    forwardNode = Node(startCell,0)
    heapq.heappush(forwardQueue, forwardNode)
    forwardCost = {startCell: 0}
    forwardVisited = {startCell: [startCell]}
    
    backwardQueue = []
    backwardNode = Node(goalCells[0], 0)
    heapq.heappush(backwardQueue, backwardNode)
    backwardVisited = {goalCells[0]: [goalCells[0]]}
    backwardCost = {goalCells[0]: 0}
    
    visitedIntersection = None
    def manhattanDistance(a,b):
        result = abs(a.x -b.x) + abs(a.y -b.y)
        return result
   
    while forwardQueue and backwardQueue:
        forward = heapq.heappop(forwardQueue).cell
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+forward.x, move[1]+forward.y)
            if nextNode is None or nextNode.isWall() or  nextNode in forwardVisited:
                continue
            
            new_cost = forwardCost[forward] + 1
            
            if nextNode not in forwardCost or new_cost < forwardCost[nextNode]:
                forwardCost[nextNode] = new_cost
                priority = new_cost + manhattanDistance(nextNode, goalCells[0])
                temp = Node(nextNode,priority)
                if draw:
                    nextNode.setVisited(True)
                    grid.drawNode(nextNode)
                forwardVisited[nextNode] = forwardVisited[forward] + [nextNode]
                heapq.heappush(forwardQueue, temp)
            
            if nextNode in backwardVisited:
                visitedIntersection = nextNode
                break
        if visitedIntersection is not None:
            break
        
        backward = heapq.heappop(backwardQueue).cell
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+backward.x, move[1]+backward.y)
            if nextNode is None or nextNode.isWall() or  nextNode in backwardVisited:
                continue
                        
            new_cost = backwardCost[backward] + 1
            
            if nextNode not in backwardCost or new_cost < backwardCost[nextNode]:
                backwardCost[nextNode] = new_cost
                priority = new_cost + manhattanDistance(nextNode, startCell)
                temp = Node(nextNode,priority)
                if draw:
                    nextNode.setVisited(True)
                    grid.drawNode(nextNode)
                backwardVisited[nextNode] = backwardVisited[backward] + [nextNode]
                heapq.heappush(backwardQueue, temp)
            
            if draw:
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
            if nextNode in forwardVisited:
                visitedIntersection = nextNode
                break
        if visitedIntersection is not None:
            break
        
    if visitedIntersection is not None:
        path = forwardVisited[visitedIntersection] + backwardVisited[visitedIntersection][::-1]
        return path
    else:
        return None

def encodePath(lst):
    string =""
    for i in range(len(lst)-1):
        if lst[i].x - lst[i+1].x ==0 and lst[i].y -lst[i+1].y == 1:
            string += "up; "
        if lst[i].x - lst[i+1].x ==1 and lst[i].y -lst[i+1].y == 0:
            string += "left; "
        if lst[i].x - lst[i+1].x ==0 and lst[i].y -lst[i+1].y == -1:
            string += "down; "
        if lst[i].x - lst[i+1].x == -1 and lst[i].y -lst[i+1].y == 0:
            string += "right; "
    return string