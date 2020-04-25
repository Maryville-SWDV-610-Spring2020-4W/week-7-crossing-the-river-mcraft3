#crossing_the_river_graph.py
"""
SWDV-610-4W 20/SP2 DATA STRUCTURES WK 7
Module 7.11 Crossing the River.

PE1: crossing_the_river.py

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft"""
# ------------------------------------------------
"""Specified Requirements from Canvas:

Write a program that solves the following problem:

Three missionaries and three cannibals come to a
river and find a boat that holds two people.
Everyone must get across the river to continue on
the journey. However, if the cannibals ever
outnumber the missionaries on either bank, the
missionaries will be eaten.

Find a series of crossings that will get everyone
safely to the other side of the river.  Record
your program running and submit your code and
recording.

In addition to coding this task, you must post a
video running and explaining your code.  This
allows for you to demonstrate what is occurring in
the code as it is happening and how it is
organized.  You must also run your code in the
video to explain the output and why the program
produced that output.

Please upload your video to Canvas and make sure
it is not a .flv.  I prefer .mp4's.
"""
# ------------------------------------------------
"""GitHub Submission Instructions:
Once you complete these exercises, be sure you
have committed your solutions locally and pushed
them up to the remote repository. If you are
unsure how to clone the repository for this
assignment, please review Pull and Push for
Assignments.

GitHub Link:
https://classroom.github.com/a/FZrZZ3AK"""
# ------------------------------------------------
"""Canvas Submission Instructions:

When you have completed this assignment and pushed
your work to the remote GitHub repository, answer
the following question(s):

    How many hours do you estimate you used
    completing this assignment?
    
    What was easiest for you when completing this
    assignment?
    
    What was the most difficult challenge you
    experienced when completing this assignment?

To begin, click the Submit Assignment button in
Canvas and respond in the available text entry
box."""
# ------------------------------------------------
"""Cannibals and Missionaries Rubric

1. Readability - Code is well organized,
   descriptive, and readable

2. Initialized States - Program starts in the
   proper state.

3. Output - Visual display of program going
   through the moves to move cannibals and
   missionaries. Must be readable and 
   understandable to a layperson (not just a list
   of state changes).
 
4. Move set - Program can complete the cycle in
   a certain amount of moves.

5. Video Explanation - Video clearly explains the
   structure of the code and how it is being
   excited. Includes a clear display of the code
   running.
   
6. Answers all canvas questions.

7. Video Submission - Clearly explains the
   organization and output of programs.
"""
# ------------------------------------------------
from adj_list_graph import Graph 
from doublyLinkedQueue import Queue
# ------------------------------------------------
"""The crossRiverGraph function builds the full
graph for an n-by-n board, in this scenario a
25x25 is used. The crossRiverGraph calls two
helper functions: posToNodeId and genLegalMoves.

The aim of this program was to have the equivalent
of a start vector of (3,3,1) or (3,3) and a finish
vector or equivalent offest of of (0,0,0)  or
simply (0,0) to represent moving to the other side
of the river. This program does not implement an
actual vector class or a state machine class and
simply uses a graph and DFS/BFS."""
def crossRiverGraph(bdSize):
    crGraph = DFSGraph()  
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)         # vertex ID / coord
            newPositions = genLegalMoves(row,col,bdSize) # vertex neighbors/connected list
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdSize)
                crGraph.addEdge(nodeId,nid)              # add vertex, add edge
    return crGraph
# ------------------------------------------------
"""posToNodeId is a helper function to
crossRiverGraph converts a location on the board
in terms of a row and a column into a linear
vertex number."""

def posToNodeId(row, column, board_size):                # converts position to vertex coord
    return (row * board_size) + column

# ------------------------------------------------
"""genLegalMoves is a helper function called by
crossRiverGraph. At each square on the board,
crossRiverGraph calls genLegalMoves to create a
list of legal moves for that position on the
board. All legal moves are then converted into
edges in the graph."""
def genLegalMoves(x,y,bdSize): # generate up to 10 edges/moves that are on board
    newMoves = []              #  provides connected to list for a vertex/node
    moveOffsets = [(-1,-0),(-2,-0),(-0,-1),(-0,-2),(-1,-1),
                   (1,0),(2,0),(0,1),(0,2),(1,1)]

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # calls helper verifies on board
        if legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize):
            newMoves.append((newX,newY)) # edges
    return newMoves 

# ------------------------------------------------
"""legalCoord is a helper function for
genLegalMoves, and makes sure that a particular
move generated is still on the board."""
# calls twice
# verify row x is 0 to bdsize
# verify col y is 0 to bdsize
def legalCoord(x,bdSize):     
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
# ------------------------------------------------
"""Provides Breadth First Search (BFS) algorithm
to find the shortest solution to a graph problem.

Builds a tree, one level of the tree at a time. A
breadth first search adds all children of the
starting vertex before it begins to discover any
of the grandchildren."""
def bfs(g,start):
    # BFS begins at starting vertex s
    # initialize distance to 0 for starting vertex
    start.setDistance(0) 
    
    # Initialize predecessor to None start vertex
    start.setPred(None)  
    vertQueue = Queue() # create queue
    vertQueue.enqueue(start) # put start in queue
    
    # begin exploring vertices at front of queue
    # by iterating over its adjacency list
    # (ConnectedTo) via getConnections.
    while (vertQueue.size() > 0):
        # dequeue and make current
        currentVert = vertQueue.dequeue()
        
        # get connections of current
        for nbr in currentVert.getConnections():
            
            # check color, if white, unexplored.
            if (nbr.getColor() == 'white'):
                
                # color gray to show currently
                # being explored
                nbr.setColor('gray')
                
                # Distance set to distance
                # currentVert + 1
                nbr.setDistance(currentVert.getDistance() + 1)
                
                # Predecessor set to currentVert
                nbr.setPred(currentVert)
                
                # Add to end of queue
                # Schedules this vertex for
                # further exploration, after
                # adjacency list processed.
                vertQueue.enqueue(nbr)
                
        # Explore complete for this vertice.
        # No remaining white / unexplored vertices
        # adjacent.
        currentVert.setColor('black')

# ------------------------------------------------
# Shows how to follow the predecessor links to
# print out the path
def traverse(y, outfile):
    x = y
    while (x.getPred()):
        
        # prints to file to export data
        print("{} ".format(x.getID()), end="", file=outfile)
        x = x.getPred()
    #print("", x.getID(), "", end="")
    print("{} ".format(x.getID()), end="", file=outfile)

# ------------------------------------------------
# extends Graph class by adding time tracker
# and adds methods dfs and dfsvisit
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        # tracks time across calls        
        self.time = 0
        
# ------------------------------------------------    
    # DFS Search
    def dfs(self, pathDFScr):
        # iterates over all vertices in the graph
        # ensures all nodes in graph are
        # considered and no vertices are left out
        # of the depth first forest.
        # iterave over DFSGraph or self.        
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                
                # if vertice white, call dfsvisit
                self.dfsvisit(aVertex, pathDFScr)
        return pathDFScr
    
# ------------------------------------------------
    # Helper function for DFS
    def dfsvisit(self,startVertex, pathDFScr):
        # starts with single vertex and explores
        # all of the neighboring white vertices
        # as deeply as possible.
    
        startVertex.setColor('gray')                    # set gray, being explored
        self.time += 1                                  # increment time tracker
        startVertex.setDiscovery(self.time)             # start discovery tracker
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':        # if white explore, if black done
                nextVertex.setPred(startVertex)         # set predecessor
                self.dfsvisit(nextVertex, pathDFScr)    # call next explore
        startVertex.setColor('black')                   # set black, complete branch
        
        # provides means to print path
        # will be in reverse order of predecessors
        # (path back to start; reverse it)
        # appends key to path
        pathDFScr.append(startVertex.getID()) 
        self.time += 1                                 # increment time for vertex
        startVertex.setFinish(self.time)               # for vertex
        return pathDFScr
        # return path
        
# ------------------------------------------------
def main():
    
    pathDFScr = []                            
    crGraph = crossRiverGraph(25)             
    crGraph.dfs(pathDFScr)                    
    print()
    print("Size of Cross the River Graph, all nodes/vertices:", crGraph.get_numVertices())    

    outfile = open("bfsoutfile.txt", "w")  # 384, 390    for 25x25 graph, LL 0,0 (625 nodes/vertices)
                                           #   312       left x axis bottom 0 over to 24
                                           # 234, 240    left y axis bottom 0 up to 24
    
    bfs(crGraph, crGraph.getVertex(312))   # 312-390, path 73. 234-312, path 73 L to R up
                                           # 384-312, path 79. 312-240, path 79 L to R down 
    
    traverse(crGraph.getVertex(390), outfile)  # break 240-312, 312-384 R to L up
    outfile.close()                            # break 390-312, 312-234 L to R down

    # open the file
    infile = open( "bfsoutfile.txt", 'r' ) # file saved from running bfs
    bfspath = infile.read()                # ingest file
    bfspath = bfspath.rstrip()             # remove white space
    bfspathlist = bfspath.split()          # print below for finish to start
    
    print("\nBFS path extracted from Graph / BFS method using BFS Traverse method of BFS,")
    print("shown order finish to start:\n")
    for i in bfspathlist:                  # print each vertex/key in list path
        print((i) + ',', end=" ")          # append print vice new line    
    
    bfspathlist.reverse()                  # print below for start to finish
    print("\n\nBFS path extracted from Graph / BFS method using BFS Traverse method of BFS,")
    print("shown after reversing, order start to finish:\n")
    
    for i in bfspathlist:                  # print each vertex/key in list path
        print((i) + ',', end=" ")          # append print vice new line
    
    print("\n\nLength of BFS Path:", len(bfspathlist))
    infile.close()                         # close file, don't leave it open
        
main()