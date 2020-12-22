from Model import *
from collections import deque
from queue import *
from BFS import *


test1_card = Card("R", 1)
test2_card = Card("R", 1)
test3_card = Card("R", 6)
test4_card = Card("G", 1)
test5_card = Card("G", 5)
test6_card = Card("G", 3)
test7_card = Card("G", 3)
test8_card = Card("G", 2)
test9_card = Card("G", 9)
test10_card = Card("G", 10)

test1_batch = Batch()
test2_batch = Batch()
test3_batch = Batch()
test4_batch = Batch()

test1_batch.insert_card(test3_card)
test1_batch.insert_card(test4_card)
test1_batch.insert_card(test8_card)
# test1_batch.insert_card(test1_card)




test2_batch.insert_card(test3_card)
test2_batch.insert_card(test5_card)
test2_batch.insert_card(test8_card)
# test2_batch.insert_card(test1_card)
# test2_batch.insert_card(test5_card)



test3_batch.insert_card(test4_card)
test3_batch.insert_card(test5_card)
test3_batch.insert_card(test7_card)
test3_batch.insert_card(test8_card)
# test3_batch.insert_card(test1_card)

test4_batch.insert_card(test4_card)
test4_batch.insert_card(test5_card)
test4_batch.insert_card(test7_card)
test4_batch.insert_card(test8_card)

batch_list_1 = [test1_batch, test3_batch]
batch_list_2 = [test1_batch, test2_batch]

test1_state = State(2, 6, batch_list_1, None, 0, None, 65)
test2_state = State(2, 0, batch_list_2, None, 0, None, 588)


# q = Queue()
# q.put_nowait(test1_state)
# q.put_nowait(test2_state)
# print(q.qsize())
# print(q.get_nowait())
q = PriorityQueue()
#
q.put_nowait(test1_state)
q.put_nowait(test2_state)
# q.put_nowait("reza")
# q.put_nowait("amir")

#
print(q.get_nowait())
print(q.get_nowait())
# print(q.get_nowait()[1])
# print(q.get_nowait()[1])

# print("================================================================================")
#
# print(hash(test1_state))
# print(test1_state)
# print("\n")
# test1_state.next_states()
#
# print(hash(test1_state))
# print(hash(test2_state))
# test_IO = IO()
# print(test_IO.read())

# s = set()
# s.add(test1_state)
#
# print(test1_state in s)
# print(test2_state in s)


#

# bfs = BFS()
# bfs.frontier.put(5)
# bfs.frontier.put(3)
# bfs.frontier.put(1)
# print(bfs.frontier.get())
# print(bfs.frontier.get())
# print(bfs.find_frontier(6))



