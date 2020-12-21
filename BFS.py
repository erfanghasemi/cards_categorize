from Model import *
from queue import *


class BFS:
    def __init__(self):
        self.goal_state = None
        self.io_handler = IO()
        self.init_state = self.io_handler.read()
        self.expanded_nodes = 0
        self.created_nodes = 0
        self.frontier = Queue()
        self.frontier.put_nowait(self.init_state)
        self.explored = {}

    def search(self):
        if self.init_state.goal_test():
            self.goal_state = self.init_state
            self.io_handler.write(self.goal_state.cost, self.expanded_nodes, self.created_nodes)
            return 1

        while True:
            if self.frontier.empty():
                print("Failure  :( ")
                return -1
            state = self.frontier.get_nowait()
            self.explored[hash(state)] = state



