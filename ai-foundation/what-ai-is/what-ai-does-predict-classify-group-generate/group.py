# Group (clustering, with k-means): find groups in data that comes with no answers at all.
# Made-up customers: (visits a month, dollars spent a visit). Nobody has labelled them.

customers = [(2, 85), (6, 40), (7, 45), (3, 90), (12, 14), (5, 38), (1, 75), (14, 18), (11, 10)]


def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


centres = customers[:3]  # start: the first three customers are the centres of three groups
for _ in range(10):
    # put each customer in the group whose centre is nearest
    groups = [[] for _ in centres]
    for i, c in enumerate(customers):
        groups[min(range(3), key=lambda g: distance(c, centres[g]))].append(i)
    # move each centre to the middle of its group
    centres = [(sum(customers[i][0] for i in g) / len(g),
                sum(customers[i][1] for i in g) / len(g)) for g in groups]

for n, (g, (visits, spend)) in enumerate(zip(groups, centres), start=1):
    members = ", ".join(str(i + 1) for i in g)
    print(f"group {n}: customers {members} (about {visits:.0f} visits, ${spend:.0f} a visit)")
print("the groups have no names: what each one means is yours to decide")
