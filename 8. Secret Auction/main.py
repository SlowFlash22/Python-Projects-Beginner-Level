from art import logo

bidders = {}
winName = ''
winValue = -1

def Winner(bidders):
    max = 0
    for x in bidders:
        if bidders[x]>max:
            max = bidders[x]
            winName = x
    from art import winner
    print(winner)
    print('----------------------------------')
    print(f"{winName} wins at ${max}")
    print('----------------------------------')


game_on = True
while game_on:
    from art import welcome
    print(logo)
    print(welcome)
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? 'Yes' or 'No'\n").title()
    if should_continue == 'No':
        game_on = False
    from clear import clean
    clean()
    
Winner(bidders)

