from Model import *
from queue import *


class DLS:
    def __init__(self, limit, init_state):
        self.goal_state = None
        self.io_handler = IO()
        self.init_state = init_state
        self.expanded_nodes = 0
        self.created_nodes = 1
        self.limit = limit
        self.frontier = LifoQueue()

    def search(self):
        self.frontier.put_nowait(self.init_state)

        if self.init_state.goal_test():
            self.goal_state = self.init_state
            return self.expanded_nodes, self.created_nodes, self.goal_state

        while True:

            if self.frontier.empty():
                return self.expanded_nodes, self.created_nodes, None

            state = self.frontier.get_nowait()

            self.expanded_nodes += 1

            if state.goal_test():
                self.goal_state = state
                return self.expanded_nodes, self.created_nodes, self.goal_state

            if state.cost != self.limit:
                childes = state.next_states()

            if state.cost == self.limit:
                if state.goal_test():
                    self.goal_state = state
                    return self.expanded_nodes, self.created_nodes, self.goal_state
                continue

            for child in childes:
                self.created_nodes += 1
                self.frontier.put_nowait(child)







