from itertools import permutations, combinations

n = 8
x = range(1, n+1)

def is_diag(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    gradient = (y2-y1)/(x2-x1)
    if gradient == -1 or gradient == 1:
        return(True)
    else:
        return(False)

list_of_permutations = []

for permuation in permutations(range(1, n+1)):
    y = permuation
    all_permutations = list(zip(x,y))
    list_of_permutations.append(all_permutations)

for possible_solution in list_of_permutations:
    solutions = []
    for piece1, piece2 in combinations(possible_solution, 2):
        solutions.append(is_diag(piece1, piece2))

    if True not in solutions:
        print(possible_solution)