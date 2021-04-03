import numpy as np
import itertools

def battle(player1, player2):
    results = {"player1": [],
              "player2": []}
    for i in itertools.zip_longest(player1, player2):
        i = list(i)
        if i[0] is None:
            i[0] = [0,0]
        elif i[1] is None:
            i[1] = [0,0]
        result = np.subtract(i[0],np.flip(i[1], 0))
        if result[0] == 0 and result[1] == 0:
            continue
        elif result[0] < 0 and result[1] >0:
            results["player1"].append(i[0])
            results["player2"].append(i[1])
        elif result[0] >= 0 and result[1] >= 0:
            results["player1"].append(i[0])
        elif result[0] <= 0 and result[1] <= 0:
            results["player2"].append(i[1])
    return results



player1 = [[1, 1], [2, 1], [2, 2], [5, 5]]
player2 = [[1, 2], [1, 2], [3, 3]]

player1 = [[2, 3], [1, 4]]
player2 = [[3, 3], [4, 1]]

#player1 = [[2, 3], [1, 4]]
#player2 = [[3, 3], [4, 1]]
print(battle(player1, player2))
