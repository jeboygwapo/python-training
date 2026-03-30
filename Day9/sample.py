bid_db = {"Jayvee": 100,
          "Mark": 100
}
winner_list = []

highest_bid = max(bid_db.values())
for winner in bid_db:
    if highest_bid == bid_db[winner]:
        print(winner)
        break
    

# for winner in range(0, len(bid_db)-1):
#     print(winner)
#     print(len(bid_db))


