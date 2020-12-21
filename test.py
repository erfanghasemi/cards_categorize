from Model import *


test1_card = Card("R", 1)
test2_card = Card("R", 5)
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
test1_batch.insert_card(test2_card)
test1_batch.insert_card(test8_card)
test1_batch.insert_card(test1_card)




test2_batch.insert_card(test4_card)
test2_batch.insert_card(test8_card)
test2_batch.insert_card(test6_card)
test2_batch.insert_card(test1_card)
test2_batch.insert_card(test5_card)


# test3_batch.insert_card(test4_card)
# test3_batch.insert_card(test7_card)
# test3_batch.insert_card(test6_card)
# test3_batch.insert_card(test9_card)
# test3_batch.insert_card(test1_card)

test4_batch.insert_card(test2_card)
test4_batch.insert_card(test10_card)
test4_batch.insert_card(test7_card)
test4_batch.insert_card(test9_card)

batch_list_1 = [test1_batch, test2_batch, test3_batch, test4_batch]
# batch_list_2 = [test1_batch, test3_batch]

print("================================================================================")
test1_state = State(4, 0, batch_list_1, None, 0)
print(test1_state)
print("\n")
test1_state.next_states()
# test2_state = State(2, 1, batch_list_2, None, 0)

