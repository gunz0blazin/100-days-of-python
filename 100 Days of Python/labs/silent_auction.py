def get_bids():
#set empty dictionary and status for input loop
    test_dic ={}
    should_continue = "yes"
#input bids
    while should_continue == "yes":
        name = input("name? \n")
        bid = int(input("bid? \n$"))
        test_dic[name] = bid
        should_continue = input("another bid? yes or no \n")
        print ("\n"*100)
#find highest bid
    winner = ""
    high_bid = 0
    for bidder in test_dic:
        bid_amount = test_dic[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
#print winner  
    print (f"the winner is {winner} with ${high_bid}")

get_bids()
