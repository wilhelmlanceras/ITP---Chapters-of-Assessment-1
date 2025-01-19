rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nRivers included in this dataset:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries included in this dataset:")
for country in rivers.values():
    print(f"- {country.title()}")