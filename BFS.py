from Model import *


test1_card = Card("R", 1)
test2_card = Card("G", 2)
test3_card = Card("R", 6)
test4_card = Card("G", 4)
test5_card = Card("R", 5)
test6_card = Card("Y", 9)
test7_card = Card("R", 7)
test8_card = Card("B", 8)
test9_card = Card("Y", 9)
test10_card = Card("B", 15)

test1_batch = Batch()
test2_batch = Batch()
# print(test1_batch.is_empty())
# print(test10_card.__str__())
print(test1_batch.sorted_until)
test1_batch.insert_card(test3_card)
print(test1_batch.sorted_until)
test1_batch.insert_card(test2_card)
print(test1_batch.sorted_until)
test1_batch.insert_card(test1_card)
print(test1_batch.sorted_until)
print(test1_batch.cards_count)

print(test1_batch.is_sorted())
# test2_batch.insert_card(test1_card)
# test2_batch.insert_card(test2_card)
# print(test1_batch.is_empty())

# print(test1_batch.last_card_number())
# print(test1_batch.last_card_number())
# print(test1_batch == test2_batch)
print(test1_batch.__str__())



