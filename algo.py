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
    node = 1
    while queue: #while queue not empty
        current = queue.popleft() #pop the first element
        
        if draw: #visualise when required      
            current.setVisited(True)
            current.setFrontier(False)
            grid.drawNode(current)
        if current in goalCells: #current is goal
            path = visited[current]
            return path, node
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            if nextNode is None or nextNode in visited or nextNode.isWall(): #if the next node is none or already visited or a wall
                continue           
            
            visited[nextNode] = visited[current] + [nextNode] #return a list of parent nodes
            node +=1
            queue.append(nextNode)
            
            if draw: #visualise when required
                nextNode.setFrontier(True)
                grid.drawNode(nextNode)
    
    return None, node

def DFSRecursivesearch(grid, draw= True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    class Node:
        def __init__(self):
            self.value =1
    node = Node()
    #recursive function will return the path list in correct order
    def dfs(cur, visited): #recursive function, visited is the list of visited nodes
        if cur in goalCells:
            return [cur]
        moves = [(0,-1),(-1,0),(0,1),(1,0)] # up, left, down, right
        for i, j in moves:
            nextNode = grid.locateCellCoord(i+cur.x, j+cur.y) #locate the next node

            if nextNode is None or nextNode.isWall() or nextNode in visited: #if the node is none or it is wall or visited
                continue
            
            

            visited.add(nextNode) #append the node into visited list
            node.value += 1
            if draw: #draw when required
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
            res = dfs(nextNode, visited) # call the function it self
            visited.remove(nextNode) #delete them from the visited list
            if res: # if there is a way then append
                return [cur] + res
            else:
                if draw: #draw when required
                    nextNode.setVisited(False)
                    grid.drawNode(nextNode)

        return None #return none when there is no way
    return dfs(startCell, {startCell}),node.value



def DFSsearch(grid,draw=True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    path = []
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    moves = [(0,-1),(-1,0),(0,1),(1,0)][::-1] # up, left, down, right
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
    
    return None, node


def ASsearch(grid, draw = True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    node = 1
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]] #up, left, down, right
    def manhattanDistance(a,goals): #heuristic function
        result = abs(a.x -goals[0].x) + abs(a.y -goals[0].y) #return the smallest distance to any of the goal cell
        for b in goals:
            temp = abs(a.x -b.x) + abs(a.y -b.y)
            if temp <result:
                result = temp
        return result
    class Node: #node to store the cell and pirority
        def __init__(self,cell,priority, count):
            self.cell = cell
            self.priority = priority #priority is calculated based on path cost and manhattan distance
            self.count = count
        
        def __lt__(self, other): #less than operator to compare between nodes
            if self.priority == other.priority:
                return self.count < other.count
            return self.priority < other.priority 
        
        def __str__(self): #to print the Node
            return f"priority: {self.priority}, cell: {self.cell}"
        
    path = [] # the path list
    visited = {startCell:None} #hash map to store parent node to trace back
    cost = {startCell: 0} #the current cost to reach to the node
    queue = []
    startCell = Node(startCell,0,node) 
    heapq.heappush(queue, startCell) #priority queue
    while queue:
        current = heapq.heappop(queue) #pop the first node from the queue with smallest value
        current = current.cell
        if draw: #visualise when required
                current.setFrontier(False)
                current.setVisited(True)
                grid.drawNode(current)
        if current in goalCells: #current is goal cell
            while current is not None : #trace back from goal cell up until start cell with visited list
                path.append(current) 
                if current.isStart():
                    break
                current = visited[current]
            path.reverse() #reverse the list to make it in correct order
           
            return path, node
        
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            if nextNode is None or nextNode in visited or nextNode.isWall(): #skip if the cell does not satisfy
                continue
            newCost = cost[current] + 1 #each cell will cost 1 to travel
            # Check if the neighbor has not been visited or the new cost is lower
            if nextNode not in cost or newCost < cost[nextNode]: 
                cost[nextNode] = newCost # Update the cost and add the neighbor to the priority queue
                priority = newCost + manhattanDistance(nextNode, goalCells)
                node += 1
                temp = Node(nextNode,priority,node)
                heapq.heappush(queue, temp)
                
                if draw:
                    nextNode.setFrontier(True)
                    grid.drawNode(nextNode)
                visited[nextNode] = current
   
    return None, node

def GBFSsearch(grid, draw = True):
    startCell = grid.locateStartCell() #locate the start cell from grid
    goalCells = grid.locateGoalCells() #locate all goal cells from grid
    node = 1
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]] #up, left, down, right
    def manhattanDistance(a,goals): #heuristic function
        result = abs(a.x -goals[0].x) + abs(a.y -goals[0].y) #return the smallest distance to any of the goal cell
        for b in goals:
            temp = abs(a.x -b.x) + abs(a.y -b.y)
            if temp <result:
                result = temp
        return result
    class Node: #node to store the cell and pirority
        def __init__(self,cell,priority,count):
            self.cell = cell
            self.priority = priority #priority is calculated based manhattan distance
            self.count = count
        
        def __lt__(self, other): #less than operator to compare between nodes
            if self.priority == other.priority:
                return self.count < other.count
            return self.priority < other.priority 
        
        def __str__(self): #to print the Node
            return f"priority: {self.priority}, cell: {self.cell}"
        
    path = [] #the path list
    visited = {startCell:None} #hash map to store parent node to trace back
    queue = []
    startCell = Node(startCell,0,node) #form a node priority of zero
    heapq.heappush(queue, startCell) #priority queue to push node into queue based on the value
    while queue:
        current = heapq.heappop(queue)
        current = current.cell
        if draw: #visualise when required
                current.setFrontier(False)
                current.setVisited(True)
                grid.drawNode(current)
        if current in goalCells: #current is goal cell
            while current is not None : #trace back from goal cell up until start cell with visited list
                path.append(current) 
                if current.isStart():
                    break
                current = visited[current]
            path.reverse() #reverse the list to make it in correct order
            return path,node
        
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y) #locate the cell from the grid
            if nextNode is None or nextNode.isVisited() or nextNode.isWall(): #check if the cell satisfy the requirement
                continue
            
            if nextNode not in visited: #if the node has not been visisted
                priority = manhattanDistance(nextNode, goalCells)
                node += 1
                temp = Node(nextNode,priority,node) #make a node with priority of manhattan distance
                heapq.heappush(queue, temp) #heap push the cell based on the value
                
                if draw: #draw when required
                    nextNode.setFrontier(True)
                    grid.drawNode(nextNode)
                visited[nextNode] = current
    
    return None, node

def CUS1search(grid, draw = True): #uninformed search is bidirectional search
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    node = 2
    while goalCells: #search through all possible goals until find a path, otherwise return none
        forwardQueue = deque()
        forwardQueue.append(startCell)
        forwardVisited = {startCell: [startCell]} #the list is the path to the cell
        
        backwardQueue = deque()
        goalCell = goalCells.pop(0)
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
            for move in [(0,1),(1,0),(0,-1),(-1,0)]:
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
            
            return path, node
        else:
            if goalCells:
                if draw:
                    grid.resetGrid(True)
                else:
                     grid.resetGrid(False)
    
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
    goalCells.sort(key=lambda x: (x.x,x.y))
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    node = 1
    
    forwardQueue = []
    forwardNode = Node(startCell,0,0)
    heapq.heappush(forwardQueue, forwardNode)
    forwardCost = {startCell: 0}
    forwardVisited = {startCell: [startCell]}
    
    backwardQueue = []
    backwardVisited = {}
    backwardCost = {}
    
    for goal in goalCells:
        backwardNode = Node(goal, 0,node)
        heapq.heappush(backwardQueue, backwardNode)
        backwardVisited[goal] = [goal]
        backwardCost[goal] = 0
        node +=1
    visitedIntersection = None
    minn = float('inf')
    while forwardQueue and backwardQueue:
        forward = heapq.heappop(forwardQueue).cell
        if forward in backwardVisited:
            x = forwardCost[forward] + backwardCost[forward]
            if minn > x:
                minn = x
                visitedIntersection = forward
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
                priority = newCost + manhattanDistance1(nextNode, goalCells)
                node +=1
                temp = Node(nextNode,priority, node)
                
                if draw: #draw when required
                    nextNode.setFrontier(True)
                    grid.drawNode(nextNode)
                forwardVisited[nextNode] = forwardVisited[forward] + [nextNode]
                heapq.heappush(forwardQueue, temp)
            
        
        backward = heapq.heappop(backwardQueue).cell
        if backward in forwardVisited:
                x = forwardCost[backward] + backwardCost[backward]
                if minn > x:
                    minn = x
                    visitedIntersection = backward
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
        
        if len(forwardQueue) ==0 or  len(backwardQueue) == 0:
            break
        
        a = forwardQueue[0]
        b = backwardQueue[0]
        if minn <= max(a.priority,b.priority):
            break
        
    if visitedIntersection is not None:
        path = forwardVisited[visitedIntersection] + backwardVisited[visitedIntersection][::-1]
       
        return path, node
    
    
    return None, node
    
def encodePath(lst): #function to encode the path from cells to instruction
    if lst is None:
        return "No solution found."
    else:
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