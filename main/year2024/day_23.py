from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    adjacency = defaultdict(set)
    for i in input:
        a, b = i.split("-")
        adjacency[a].add(b)
        adjacency[b].add(a)

    triplets = find_triplets(adjacency)

    return sum(
        a.startswith("t") or b.startswith("t") or c.startswith("t")
        for a, b, c in triplets
    )


def solve_2(input: list) -> str:
    adjacency = defaultdict(set)
    for i in input:
        a, b = i.split("-")
        adjacency[a].add(b)
        adjacency[b].add(a)

    cliques = find_linked(adjacency)

    max_clique = [c for c in cliques if len(c) == max(len(a) for a in cliques)][0]

    return ",".join(sorted(max_clique))


def find_triplets(adjacency):
    triangles = set()
    for a, neighbors in adjacency.items():
        for b in neighbors:
            for c in neighbors:
                if c in adjacency[b]:
                    triangles.add(tuple(sorted((a, b, c))))

    return triangles


def find_linked(adjacency):
    cliques = []

    def bron_kerbosch(r, p, x):
        if not p and not x:
            cliques.append(r)
            return
        for v in list(p):
            bron_kerbosch(r | {v}, p & adjacency[v], x & adjacency[v])
            p.remove(v)
            x.add(v)

    bron_kerbosch(set(), set(adjacency.keys()), set())

    return cliques


if __name__ == "__main__":
    input = read("day23-01.txt", "main/year2024/resources")
    print(solve_1(input))  # 1230
    print(solve_2(input))  # az,cj,kp,lm,lt,nj,rf,rx,sn,ty,ui,wp,zo
