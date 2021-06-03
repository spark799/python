guests = ["Spongebob", "Patrick", "Squidward"]

print(f"{guests[0]} you are invited to dinner.")
print(f"{guests[1]} you are invited to dinner.")
print(f"{guests[2]} you are invited to dinner.")

cant_make_it = guests.pop(2)
print(f"{cant_make_it} can't make it to dinner.")

guests.append("Sandy")
print(f"{guests[0]} you are invited to dinner.")
print(f"{guests[1]} you are invited to dinner.")
print(f"{guests[2]} you are invited to dinner.")

print("We found a bigger table.")

guests.insert(0, "Larry")
guests.insert(2, "Plankton")
guests.append("Gary")

print(f"{guests[0]} you are invited to dinner.")
print(f"{guests[1]} you are invited to dinner.")
print(f"{guests[2]} you are invited to dinner.")
print(f"{guests[3]} you are invited to dinner.")
print(f"{guests[4]} you are invited to dinner.")
print(f"{guests[5]} you are invited to dinner.")

print("I can only invite two guests.")

not_invited = guests.pop()
print(f"Sorry {not_invited} you are not invited to dinner.")
not_invited = guests.pop()
print(f"Sorry {not_invited} you are not invited to dinner.")
not_invited = guests.pop()
print(f"Sorry {not_invited} you are not invited to dinner.")
not_invited = guests.pop()
print(f"Sorry {not_invited} you are not invited to dinner.")

print(f"{guests[0]} you are still invited to dinner.")
print(f"{guests[1]} you are still invited to dinner.")

del guests[1]
del guests[0]
print(guests)