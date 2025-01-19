print ("My invitations:")
guests = ["Jesus Christ", "Albert Einstein", "Christopher Columbus"]

for guest in guests:
    invitation = "Dear " + guest + ",\nI would love to have you for dinner."
    print(invitation)
    print()

print ("Unavailable guest/s:")
unavailable_guest = "Albert Einstein"
print(unavailable_guest + " can't make it to dinner.\n")

guests[1] = "Isaac Newton"

print("New invitations:")
for guest in guests:
    invitation = "Dear " + guest +  "," + "\n" + "I would love to have you for dinner."
    print(invitation)
    print()