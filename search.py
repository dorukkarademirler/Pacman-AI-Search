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


#IMPLEMENTED RIGHT HERE

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
    stack = util.Stack()  # Using a stack for depth-first search
    stack.push((problem.getStartState(), []))  # Pushing the initial state and an empty path
    visited = []  # Keeping track of visited states to avoid cycles
    while not stack.isEmpty():
        curr, path = stack.pop()  # Popping the current state and its path
        if problem.isGoalState(curr):
            return path  # If the goal is reached, return the path
        if curr not in visited:
            visited.append(curr)  # Mark the current state as visited
            successor = problem.getSuccessors(curr)
            for elem in successor:
                new_path = path + [elem[1]]  # Extending the current path with the action
                stack.push((elem[0], new_path))  # Pushing the successor state and the new path
    return []  # Return an empty list if no solution is found


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()  # Using a queue for breadth-first search
    queue.push((problem.getStartState(), []))  # Pushing the initial state and an empty path
    visited = []  # Keeping track of visited states to avoid cycles
    while not queue.isEmpty():
        curr, path = queue.pop()  # Dequeuing the current state and its path
        if problem.isGoalState(curr):
            return path  # If the goal is reached, return the path
        if curr not in visited:
            visited.append(curr)  # Mark the current state as visited
            successors = problem.getSuccessors(curr)
            for elem in successors:
                new_path = path + [elem[1]]  # Extending the current path with the action
                queue.push((elem[0], new_path))  # Enqueuing the successor state and the new path
    return []  # Return an empty list if no solution is found


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    queue = util.PriorityQueue()  # Using a priority queue for uniform cost search
    queue.push((problem.getStartState(), []), 0)  # Pushing the initial state, an empty path, and cost 0
    visited = []  # Keeping track of visited states to avoid cycles
    while not queue.isEmpty():
        curr, curr_path = queue.pop()  # Popping the current state and its path
        if problem.isGoalState(curr):
            return curr_path  # If the goal is reached, return the path
        if curr not in visited:
            visited.append(curr)  # Mark the current state as visited
            successor = problem.getSuccessors(curr)
            for elem in successor:
                path = curr_path + [elem[1]]  # Extending the current path with the action
                cost = problem.getCostOfActions(path)
                queue.push((elem[0], path), cost)  # Pushing the successor state and the new path with updated cost
    return []  # Return an empty list if no solution is found


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    queue = util.PriorityQueue()  # Using a priority queue for A* search
    queue.push((problem.getStartState(), []), 0)  # Pushing the initial state, an empty path, and cost 0
    visited = list()
    while not queue.isEmpty():
        curr, curr_path = queue.pop()  # Popping the current state and its path
        if problem.isGoalState(curr):
            return curr_path  # If the goal is reached, return the path
        if curr not in visited:
            visited.append(curr)  # Mark the current state as visited
            successor = problem.getSuccessors(curr)
            for elem in successor:
                path = curr_path + [elem[1]]  # Extending the current path with the action
                cost = problem.getCostOfActions(path) + heuristic(elem[0], problem)
                queue.push((elem[0], path), cost)  # Pushing the successor state and the new path with updated cost
    return []  # Return an empty list if no solution is found


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
