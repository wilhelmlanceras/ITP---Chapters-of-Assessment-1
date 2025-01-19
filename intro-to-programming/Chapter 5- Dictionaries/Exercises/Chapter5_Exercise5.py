pets = []

pet = {
    'Animal type': 'Cat',
    'Name': 'Whiskers',
    'Owner': 'Aaron',
    'Age': '1 year',
    'Eats': 'Cat food',
}

pets.append(pet)

pet = {
    'Animal type': 'Dog',
    'Name': 'Buddy',
    'Owner': 'MC',
    'Age': '3 years',
    'Eats': 'Dog food',
}

pets.append(pet)

pet = {
    'Animal type': 'Rabbit',
    'Name': 'Thumper',
    'Owner': 'Tristan',
    'Age': '2 years',
    'Eats': 'Carrots',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['Name'].title() + ":")
    for key, value in pet.items():

        print("\t" + key + ": " + str(value))