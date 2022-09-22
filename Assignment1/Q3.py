list_with_dup = [12,24,35,24,88,120,155,88,120,155]
print(list_with_dup)
list_with_dup = list(set(list_with_dup))
print(list_with_dup)