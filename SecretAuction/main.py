from click import clear
from ASCII import logo

print(logo)
print("Welcome to the secret auction program.")
bidders={}
bidding_finished=False
while True:
    name=input("\nEnter  Your Name: ")
    bid=int(input("\nEnter Your bid: "))
    users=input("\nAre there any other bidders? Type 'yes' or 'no':  ").lower()
    bidders[name]=bid

    def bidding(bidding_record):
        highest_bid=0
        for bidder in bidding_record:
            bid_amount= bidding_record[bidder]
            if bid_amount> highest_bid:
                highest_bid= bid_amount
                winner=bidder
        print(f"\nThe winner is {winner} with a bid of {highest_bid}")
        # print("The highest bidder is "+max(bidders,key=bidders.get))
    if users =="no":
        bidding_finished=True
        bidding(bidding_record=bidders)
        break
    elif users =="yes":
        clear()




