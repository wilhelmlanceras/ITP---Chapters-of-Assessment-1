places_to_visit = ["Switzerland", "Japan", "Korea", "California"]

print("Original list of places to visit:")
print(", ".join(places_to_visit))
print("\nList in alphabetical order:")
print(", ".join(sorted(places_to_visit)))

print("\nOriginal list after sorted:")
print(", ".join(places_to_visit))

print("\nList in reverse alphabetical order:")
print(", ".join(sorted(places_to_visit, reverse=True)))

print("\nOriginal list after reverse sorted:")
print(", ".join(places_to_visit))

places_to_visit.reverse()
print("\nList after reverse:")
print(", ".join(places_to_visit))

places_to_visit.reverse()
print("\nList after reversing again (back to original):")
print(", ".join(places_to_visit))

places_to_visit.sort()
print("\nList after sort:")
print(", ".join(places_to_visit))

places_to_visit.sort(reverse=True)
print("\nList after sort (true):")
print(", ".join(places_to_visit))