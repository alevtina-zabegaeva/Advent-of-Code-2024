from collections import defaultdict
import itertools


filename = '23.1input.txt'
# filename = '23.1test.txt'

with open(filename) as f:
    connection_pairs = [line.strip().split('-') for line in f]

# print(connection_pairs)

connections = defaultdict(set)
for c1, c2 in connection_pairs:
    connections[c1].add(c2)
    connections[c2].add(c1)
# print(connections)

three_computers = set()
for (comp1, connections1), (comp2, connections2) in itertools.combinations(connections.items(), r=2):
    if comp1 in connections2:
        intersection = connections1 & connections2
        for comp3 in intersection:
            three_computers.add(tuple(sorted([comp1, comp2, comp3])))
print(len(three_computers))

three_t_computers = set()
for comps in three_computers:
    if any(comp[0] == 't' for comp in comps):
        three_t_computers.add(comps)
print(len(three_t_computers))
