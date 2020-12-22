from Model import *
from queue import *


class BFS:
    def __init__(self):
        self.goal_state = None
        self.io_handler = IO()
        self.init_state = None
        self.expanded_nodes = 0
        self.created_nodes = 1
        self.frontier = Queue()
        self.explored = set()

    def search(self):
        self.init_state = self.io_handler.read()
        self.frontier.put_nowait(self.init_state)

        if self.init_state.goal_test():
            self.goal_state = self.init_state
            self.io_handler = IO(self.goal_state, self.expanded_nodes, self.created_nodes)
            self.io_handler.write()
            return 1

        while True:
            if self.frontier.empty():
                print("Failure  :( ")
                return -1

            state = self.frontier.get_nowait()
            if state in self.explored:
                continue

            self.expanded_nodes += 1

            if state.goal_test():
                self.goal_state = state
                self.io_handler = IO(self.goal_state, self.expanded_nodes, self.created_nodes)
                self.io_handler.write()
                return 1

            self.explored.add(state)

            childes = state.next_states()

            for child in childes:
                if child is None:
                    continue

                if not(child in self.explored):
                    self.created_nodes += 1
                    self.frontier.put_nowait(child)


if __name__ == "__main__":
    bfs_search = BFS()
    bfs_search.search()