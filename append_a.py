# - Create a variable named `animals`
#   with the following content: `["koal", "pand", "zebr"]`
# - Add all elements an `"a"` at the end

animals = ["koal", "pand", "zebr"]
animals_2 = []

for elements in animals:                # remember that 'elements' is treated as an index and not the actual word within that list, due to which I couldn't append before
    animals_2.append(elements + 'a')
print(animals_2)


