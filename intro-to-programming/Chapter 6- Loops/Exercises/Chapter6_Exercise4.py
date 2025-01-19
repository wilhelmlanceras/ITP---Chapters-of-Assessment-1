sandwich_orders = ['grilled cheese', 'ham', 'cheese steak', 'roast beef' ' meat ball']
finished_sandwiches = []

print ("\n" "Sandwiches that are being made:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print ("\n" "Made sandwiches:")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")