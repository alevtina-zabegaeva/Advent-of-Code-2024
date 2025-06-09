from collections import defaultdict


def bron_kerbosch(current_group, potential, excluded, connections):
    if not potential and not excluded:
        if len(current_group) > 2:
            groups.append(list(current_group))
        return
    
    union_set = potential | excluded
    pivot = max(union_set, key=lambda v: len(connections[v]))
    possibles = potential - (connections[pivot])

    for vertex in possibles:
        new_group = current_group | {vertex}
        new_potential = potential & connections[vertex]
        new_excluded = excluded & connections[vertex]
        bron_kerbosch(new_group, new_potential, new_excluded, connections)
        potential.remove(vertex)
        excluded.add(vertex)


filename = '23.1input.txt'
# filename = '23.1test.txt'

with open(filename) as f:
    connection_pairs = [line.strip().split('-') for line in f]

connections = defaultdict(set)
computers = set()
for c1, c2 in connection_pairs:
    connections[c1].add(c2)
    connections[c2].add(c1)
    computers.update([c1, c2])

current_group = set()
potential = computers
excluded = set()
groups = []

bron_kerbosch(current_group, potential, excluded, connections)
groups.sort(key=lambda x: (len(x), x), reverse=True)
print(','.join(sorted(groups[0])))
