#4 kyu permutations

import itertools

def permutations(string):
    return list(set([''.join(perms) for perms in itertools.permutations([c for c in string])]))