from clearScreen import clear_screen

print("Welcome to the 5G auction program")
print("-----------------------------------\n")

auction = {}
should_continue = True

while should_continue:
    username = input("What is your name? ")
    userbid = int(input("What is your bid? $"))
    auction[username] = userbid
    other_bidders = input("Are there other bidders? Type 'yes' to continue or any other key to quit: ").lower().strip()
    clear_screen()
    if other_bidders != 'yes':
        should_continue = False

'''
highest_bidder = max(auction, key=auction.get)
highest_bid = auction[highest_bidder]
'''

highest_bid = float('-inf') # smallest possible value
highest_bidder = ""

for key, value in auction.items():
    if value > highest_bid:
        highest_bid = value
        highest_bidder = key

print(auction)
print(f"The winner is {highest_bidder} with a bid of {highest_bid}.")
