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

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    frontier = util.Stack()
    explored = []
    frontier.push((problem.getStartState(), []))
    while not frontier.isEmpty():
        current, path = frontier.pop()
        if problem.isGoalState(current):
            return path
        else:
            explored.append(current)
            for ns, a, _ in problem.getSuccessors(current):
                if ns not in explored:
                    frontier.push((ns, path+[a]))

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()
    #se creeaza o coada pt a tine nodurile ce urmeaza a fi explorate si pt a pastra ordinea in care au fost adaugate
    explored = []
    frontier.push((problem.getStartState(), []))
    while not frontier.isEmpty():
        current, path = frontier.pop()
        if current not in explored:
            explored.append(current)
            if problem.isGoalState(current):
                return path
            for ns, a, _ in problem.getSuccessors(current):
                #se verifica daca noul succesor nu a fost explorat si nu e deja in coada
                if ns not in explored and ns not in [state for state, _ in frontier.list]:
                    frontier.push((ns, path+[a]))
    return [] #daca nu se gaseste nicio cale catre "starea scop", se returneaza o lista goala

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    explored = set()
    frontier.push((problem.getStartState(), [], 0), 0)
    #starea initiala are costul zero(state, path, cost)
    while not frontier.isEmpty():
        current, path, cost = frontier.pop()
        if current in explored:
            continue #daca deja a fost explorat, sa i se dea skip
        explored.add(current)
        if problem.isGoalState(current):
            return path
        for s, a, c in problem.getSuccessors(current):
            frontier.push((s, path+[a], cost+c), cost+c)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    explored = []
    frontier.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))
    while not frontier.isEmpty():
        current, path, cost = frontier.pop()
        if not current in explored:
            explored.append(current)
            if problem.isGoalState(current):
                return path
            for s, a, c in problem.getSuccessors(current):
                frontier.push((s, path+[a], cost+c), cost+c+heuristic(s,problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
