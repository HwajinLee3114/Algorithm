import sys
input = sys.stdin.readline
shakes = list(input().strip())
cups = [0, 1, 0, 0, 2]
method = {
    'A':'12',
    'B':'13',
    'C':'14',
    'D':'23',
    'E':'24',
    'F':'34',
}

for v in shakes:
    fst = int(method[v][0])
    scd = int(method[v][1])
    cups[fst], cups[scd] = cups[scd], cups[fst]

print(cups.index(1))
print(cups.index(2))