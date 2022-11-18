inv = ["veg", "гек"]
print(*inv)
print(len(inv))
print(inv[0])
inv[1] = "хороший шит"
print(inv)
inv.append("негр")
print(inv)
for item in inv:
    print(item)
for item in inv:
    item = "Граната"

print(inv)

for i in range(len(inv)):
    inv[i] = "граната"

print(inv)

inv = ["vtg", "fdd", "dse", "fdd", "ffd"]
print(inv.index("fdd"))

print("vtg" in inv)

print("sdwe" in inv)