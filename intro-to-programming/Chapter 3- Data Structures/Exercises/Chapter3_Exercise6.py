print ("My invitations:")
guests = ["Jesus Christ", "Albert Einstein", "Christopher Columbus"]

for guest in guests:
    invitation = "Dear " + guest + ",\nI would love to have you for dinner."
    print (invitation)
    print ()

print ("Unavailable guest/s:")
unavailable_guest = "Albert Einstein"
print (unavailable_guest + " can't make it to dinner.\n")

guests [1] = "Isaac Newton"

print ("New invitations:")
for guest in guests:
    invitation = "Dear " + guest + ",\nI would love to have you for dinner."
    print (invitation)
    print ()

print("Due to limited space, I can only invite two people for dinner.\n")

while len (guests) > 2:
    removed_guest = guests.pop()
    print ("I'm sorry, " + removed_guest + ", I can't invite you to dinner.")

print ("\nThe following guests are still invited:\n")
for guest in guests:
    print ("Dear " + guest + ",\nI would love to have you for dinner.\n")

final_guest_list = ", ".join (guests)
print ("Final guest list:", final_guest_list)