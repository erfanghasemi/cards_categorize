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

    def find_frontier(self, target_state: State):
        contain = 1
        for i in range(self.frontier.qsize()):
            state = self.frontier.get_nowait()
            if state == target_state:
                contain = 0
            self.frontier.put_nowait(state)
        return contain

    def search(self):
        self.init_state = self.io_handler.read()
        self.frontier.put_nowait(self.init_state)
        if self.init_state.goal_test():
            self.goal_state = self.init_state
            # self.io_handler.write(self.goal_state.cost, self.expanded_nodes, self.created_nodes)
            print(self.goal_state)
            print("Goal is Find :)")
            return 1

        while True:

            if self.frontier.empty():
                print("Failure  :( ")
                return -1

            state = self.frontier.get_nowait()
            self.explored.add(state)
            self.expanded_nodes += 1

            childes = state.next_states()
            self.created_nodes += len(childes)

            if self.created_nodes % 1000 == 0:
                print("created Nodes = " + str(self.created_nodes))

            for child in childes:

                explored_exist = not(child in self.explored)
                frontier_exist = self.find_frontier(child)

                if explored_exist and frontier_exist:
                    if child.goal_test():
                        self.goal_state = child
                        print(self.goal_state)
                        print("Goal is Find :)")
                        print("created Nodes = " + str(self.created_nodes))
                        print("expanded Nodes = " + str(self.expanded_nodes))

                        print("depth " + str(self.goal_state.cost))
                        return 1

                    self.frontier.put_nowait(child)


if __name__ == "__main__":
    bfs_search = BFS()
    bfs_search.search()