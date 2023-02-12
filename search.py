# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfpaths(self, paths):
        """
         paths: A list of paths to take

        This method returns the total cost of a particular sequence of paths.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of paths that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    mystack = util.Stack()
    visited_nodes = []
    path = [] 

    if problem.isGoalState(problem.getStartState()):
        return []

    mystack.push((problem.getStartState(),[]))

    while True:
        if mystack.isEmpty():
            return []
        node_position, path = mystack.pop()
        visited_nodes.append(node_position)

        if problem.isGoalState(node_position):
            return path
        
        successors = problem.getSuccessors(node_position)
        if successors:
            for successor in successors:
                if successor[0] not in visited_nodes:
                    new_path = path + [successor[1]] 
                    mystack.push((successor[0],new_path))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    myqueue = util.Queue()
    visited_nodes = []
    path = [] 

    if problem.isGoalState(problem.getStartState()):
        return []

    myqueue.push((problem.getStartState(),[]))

    while True:
        if myqueue.isEmpty():
            return []
        node_position, path = myqueue.pop()
        visited_nodes.append(node_position)

        if problem.isGoalState(node_position):
            return path
        
        successors = problem.getSuccessors(node_position)
        if successors:
            for successor in successors:
                if successor[0] not in visited_nodes and successor[0] not in (state[0] for state in myqueue.list):

                    new_path = path + [successor[1]] 
                    myqueue.push((successor[0],new_path))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    myqueue = PriorityQueue()
    paths, visited_nodes = [], []

    current_node = problem.getStartState()
    myqueue.push((current_node, []), 0)

    while not myqueue.isEmpty():

        if myqueue.isEmpty():
            return []
        
        current_node, paths = myqueue.pop()

        if problem.isGoalState(current_node):
            return paths

        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            for node, direction, _ in  problem.getSuccessors(current_node):
                new_path = paths + [direction]
                priority  = problem.getCostOfActions(new_path)
                myqueue.push((node, new_path), priority )
       
    return []
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    myqueue = PriorityQueue()
    paths, visited_nodes = [], []

    current_node = problem.getStartState()
    myqueue.push((current_node, []), 0)

    while not myqueue.isEmpty():

        if myqueue.isEmpty():
            return []
        
        current_node, paths = myqueue.pop()

        if problem.isGoalState(current_node):
            return paths

        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            for node, direction, _ in  problem.getSuccessors(current_node):
                new_path = paths + [direction]
                priority  = problem.getCostOfActions(new_path)  + heuristic(node, problem)
                myqueue.push((node, new_path), priority )


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
