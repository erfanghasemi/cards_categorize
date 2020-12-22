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

    def find_frontier(self, target_state: State):
        contain = 1
        for i in range(self.frontier.qsize()):
            state = self.frontier.get_nowait()
            if state == target_state:
                contain = 0
            self.frontier.put_nowait(state)
        return contain

    def search(self):
        self.frontier.put_nowait(self.init_state)

        if self.init_state.goal_test():
            self.goal_state = self.init_state
            return self.expanded_nodes, self.created_nodes, self.goal_state

        while True:

            if self.frontier.empty():
                return self.expanded_nodes, self.created_nodes, None

            state = self.frontier.get_nowait()
            if state.cost == self.limit:
                if state.goal_test():
                    self.goal_state = state
                    return self.expanded_nodes, self.created_nodes, self.goal_state
                continue

            self.expanded_nodes += 1

            childes = state.next_states()

            if state.goal_test():
                self.goal_state = state
                return self.expanded_nodes, self.created_nodes, self.goal_state

            for child in childes:
                self.created_nodes += 1
                self.frontier.put_nowait(child)

