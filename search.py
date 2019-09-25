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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    estado_inicial = problem.getStartState()

    # nó ← um nó ESTADO = problema.ESTADO-INICIAL, CUSTO-DE-CAMINHO = 0 e CUSTO-OBJETIVO ← heurística(nó .ESTADO)
    no = No(estado=estado_inicial, custo_caminho=0, custo_objetivo=heuristic(estado_inicial, problem))

    # borda ← fila de prioridade ordenada por (CUSTO-OBJETIVO + CUSTO-DE-CAMINHO) com nó como único elemento
    # utiliza a estrutura já pronta no util
    borda = util.PriorityQueue()
    borda.push(no, priority=no.custo_total)

    # faz o processo iterativo da funcao A*
    no_final = iterate_a_star(borda, problem, heuristic)

    acoes = []
    while no_final.acao:
        acoes.append(no_final.acao)
        no_final = no_final.pai

    return acoes[::-1]


def iterate_a_star(borda, problem, heuristic):
    """
    Funcao que implementa a parte iterativa da funcao aStar. (varre a fila "borda")

    Retorna o nó final.
    """
    explorado = []
    # while borda != ∅ do
    while not borda.isEmpty():
        # nó ← POP(borda) {escolhe o nó de menor custo na borda}
        no = borda.pop()

        if no.estado in explorado:
            continue

        # explorado ← explorado ∪ nó.ESTADO
        explorado.append(no.estado)

        # if problema.TESTE-OBJETIVO(n ́o.ESTADO) then
        if problem.isGoalState(no.estado) == True:
            return no

        for estado_filho, acao, custo_caminho in problem.getSuccessors(no.estado):
            # filho ← NÓ FILHO(problema, ńo, ac̃ao)
            no_filho = No(estado_filho, custo_caminho + no.custo_caminho, heuristic(estado_filho, problem),
                          acao=acao, pai=no)
            # if filho.ESTADO não est́a na borda nem no explorado then
            if no_filho.estado not in explorado:
                borda.push(no_filho, no_filho.custo_total)
    return no


class No(object):
    """
        Classe que define o nó do problema A*

        Tem estado, o custo caminho, o custo_objetivo (dado pela a heuristica), a acao a ser
        tomada e o nó pai.

        Calcula também o custo total
    """

    def __init__(self, estado, custo_caminho, custo_objetivo, acao=None, pai=None):
        self.estado = estado
        self.custo_caminho = custo_caminho
        self.custo_objetivo = custo_objetivo
        self.acao = acao
        self.pai = pai

    @property
    def custo_total(self):
        return self.custo_caminho + self.custo_objetivo


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
