from simpleai.search import *
from simpleai.search.viewers import BaseViewer, WebViewer, ConsoleViewer

import CavernaBuilder as cb
import math

GOAL = (26, 26)
INITIAL = (18, 18)
graph = cb.build()  # caverna

listOfDoors = [((1, 2), (1, 3)), ((2, 3), (2, 2)), ((3, 4), (4, 4)), ((4, 5), (3, 5))]  # Lista de portas fechadas

# print(graph) imprime caverna com todas as portas

# fechar as portas
for i in listOfDoors:
    if i[0] in graph and i[1] in graph:
        graph[i[0]].remove(i[1])
        graph[i[1]].remove(i[0])


# print(graph) imprime caverna com as portas fechadas

class Problem(SearchProblem):

    def __init__(self, initial, goal, graph):
        SearchProblem.__init__(self, initial)
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return self.graph[state]

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == GOAL

    #    def heuristic(self, state):
    # how far are we from the goal?
    #        wrong = sum([1 if state[i] != GOAL[i] else 0
    #                     for i in range(len(state))])
    #        missing = len(GOAL) - len(state)
    #        return wrong + missing

    def heuristic(self, state):
        return math.sqrt(math.pow(state[0] - self.goal[0], 2) + math.pow(state[1] - self.goal[1], 2))

    def value(self, state):
        return sum(1 if state[i] == GOAL[i] else 0
                   for i in range(min(len(GOAL), len(state))))


#    def value(self, state):
#        return -math.sqrt(math.pow(state[0] - self.goal[0], 2) + math.pow(state[1] - self.goal[1], 2))

problem = Problem(INITIAL, GOAL, graph)
my_viewer = ConsoleViewer()
my_viewer2 = ConsoleViewer()
my_viewer3 = ConsoleViewer()
result = astar(problem, graph_search=True, viewer=my_viewer2)
result2 = breadth_first(problem, graph_search=True, viewer=my_viewer)
result3 = hill_climbing(problem, viewer=my_viewer3)

# Ex1
# print("BFS")
# print(result2.state)
# print(result2.path())
# print(f"Cost = {result2.cost}")
# print(my_viewer.stats)
# print(my_viewer.events)

# Ex2
# print("A*")
# print(result.state)
# print(result.path())
# print(f"Cost = {result.cost}")
#print(my_viewer2.stats)

# Ex3
# print("Hill Climbing")
# print(result3.state)
# print(result3.path())
# print(f"Cost = {result3.cost}")
print(my_viewer3.stats)
