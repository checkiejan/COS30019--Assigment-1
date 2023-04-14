from grid import Grid
from collections import deque
from queue import PriorityQueue

import heapq
def BFSsearch(grid):
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    visited = {startCell:None}
    queue = deque([startCell])
    while queue:
        current = queue.popleft()
        if current in goalCells:
            while current is not None : 
                path.append(current)
                if current.isStart():
                    break
                current = visited[current]
            path.reverse()
            return path
        
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            
            if nextNode is None or nextNode.isVisited() or nextNode.isWall():
                continue
            
            nextNode.setVisited(True)
            visited[nextNode] = current
            queue.append(nextNode)
            grid.drawNode(nextNode)
            
    return None

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

def DFSsearch(grid):
    startCell = grid.locateStartCell()
    goalCells = grid.locateGoalCells()
    def dfs(cur, visited):
        if cur in goalCells:
            return [cur]

        for i, j in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            nextNode = grid.locateCellCoord(i+cur.x, j+cur.y)

            if nextNode is None or nextNode.isWall() or nextNode in visited:
                continue


            visited.add(nextNode)
            nextNode.setVisited(True) #
            grid.drawNode(nextNode) #
            res = dfs(nextNode, visited)
            visited.remove(nextNode)
            if res:
                return [cur] + res

        return []
    return dfs(startCell, {startCell})

def ASsearch(grid):
    startCell = grid.locateStartCell()
    goalCells = grid.locateGoalCells()
    
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    def manhattanDistance(a,goals):
        result = abs(a.x -goals[0].x) + abs(a.y -goals[0].y)
        for b in goals:
            temp = abs(a.x -b.x) + abs(a.y -b.y)
            if temp <result:
                result = temp
        return result
    class Node:
        def __init__(self,cell,priority):
            self.cell = cell
            self.priority = priority
        
        def __lt__(self, other):
            return self.priority < other.priority 
        
        def __str__(self):
            return f"priority: {self.priority}, cell: {self.cell}"
        
    path = []
    visited = {startCell:None}
    cost = {startCell: 0}
    queue = []
    startCell = Node(startCell,0)
    heapq.heappush(queue, startCell)
    while queue:
        current = heapq.heappop(queue)
        current = current.cell
        if current in goalCells:
            while current is not None : 
                path.append(current)
                if current.isStart():
                    break
                current = visited[current]
            path.reverse()
            return path
        
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            if nextNode is None or nextNode in visited or nextNode.isWall():
                continue
            new_cost = cost[current] + 1
            
            if nextNode not in cost or new_cost < cost[nextNode]:
                cost[nextNode] = new_cost
                priority = new_cost + manhattanDistance(nextNode, goalCells)
                temp = Node(nextNode,priority)
                heapq.heappush(queue, temp)
                
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
                visited[nextNode] = current
    return None

def GBFSsearch(grid):
    startCell = grid.locateStartCell()
    goalCells = grid.locateGoalCells()
    
    moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    def manhattanDistance(a,goals):
        result = abs(a.x -goals[0].x) + abs(a.y -goals[0].y)
        for b in goals:
            temp = abs(a.x -b.x) + abs(a.y -b.y)
            if temp <result:
                result = temp
        return result
    class Node:
        def __init__(self,cell,priority):
            self.cell = cell
            self.priority = priority
        
        def __lt__(self, other):
            return self.priority < other.priority 
        
        def __str__(self):
            return f"priority: {self.priority}, cell: {self.cell}"
        
    path = []
    visited = {startCell:None}
    cost = {startCell: 0}
    queue = []
    startCell = Node(startCell,0)
    heapq.heappush(queue, startCell)
    while queue:
        current = heapq.heappop(queue)
        current = current.cell
        if current in goalCells:
            while current is not None : 
                path.append(current)
                if current.isStart():
                    break
                current = visited[current]
            path.reverse()
            return path
        
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+current.x, move[1]+current.y)
            if nextNode is None or nextNode.isVisited() or nextNode.isWall():
                continue
            new_cost = cost[current] + 1
            
            if nextNode not in cost or new_cost < cost[nextNode]:
                cost[nextNode] = new_cost
                priority = manhattanDistance(nextNode, goalCells)
                temp = Node(nextNode,priority)
                heapq.heappush(queue, temp)
                
                nextNode.setVisited(True)
                grid.drawNode(nextNode)
                visited[nextNode] = current
    return None

def CUS1search(grid):
    startCell = grid.locateStartCell()
    path = []
    goalCells = grid.locateGoalCells()
    moves = [(0,-1),(-1,0),(0,1),(1,0)]
    
    forwardQueue = deque()
    forwardQueue.append(startCell)
    forwardVisited = {startCell: [startCell]}
    
    backwardQueue = deque()
    backwardQueue.append(goalCells[0])
    backwardVisited = {goalCells[0]: [goalCells[0]]}
    
    visitedIntersection = None
    
    while forwardQueue and backwardQueue:
        forward = forwardQueue.popleft()
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+forward.x, move[1]+forward.y)
            if nextNode is None or nextNode.isWall() or  nextNode in forwardVisited:
                continue
            
            forwardQueue.append(nextNode)
            forwardVisited[nextNode] = forwardVisited[forward] + [nextNode]
            nextNode.setVisited(True)
            grid.drawNode(nextNode)
            if nextNode in backwardVisited:
                visitedIntersection = nextNode
                break
        if visitedIntersection is not None:
            break
        
        backward = backwardQueue.popleft()
        for move in moves:
            nextNode = grid.locateCellCoord(move[0]+backward.x, move[1]+backward.y)
            if nextNode is None or nextNode.isWall() or  nextNode in backwardVisited:
                continue
            
            backwardQueue.append(nextNode)
            backwardVisited[nextNode] = backwardVisited[backward] + [nextNode]
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