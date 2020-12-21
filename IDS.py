from Model import *
from DLS import *


class IDS:
    def __init__(self, limit):
        self.io_handler = IO()
        self.init_state = None
        self.expanded_nodes = 0
        self.created_nodes = 0
        self.limit = limit
        self.goal_state = None

    def search(self):
        self.init_state = self.io_handler.read()

        for level in range(0, self.limit+1):
            dls_search = DLS(level, self.init_state)
            info = dls_search.search()
            self.expanded_nodes += info[0]
            self.created_nodes += info[1]
            self.goal_state = info[2]

            if self.goal_state is not None:
                self.io_handler = IO(self.goal_state, self.expanded_nodes , self.created_nodes)
                self.io_handler.write()
                return 1


if __name__ == "__main__":
    ids_search = IDS(9)
    ids_search.search()