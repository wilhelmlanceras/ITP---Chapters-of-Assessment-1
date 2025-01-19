sandwich_orders = ['grilled cheese', 'pastrami', 'pastrami', 'pastrami', 'ham', 'cheese steak', 'roast beef' ' meat ball']
finished_sandwiches = []

print ("\n" "Sorry we ran out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
print ("\n" "Sandwiches that are being made:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print ("\n" "Made sandwiches:")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")