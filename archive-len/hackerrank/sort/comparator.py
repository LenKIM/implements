from functools import cmp_to_key


class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):
        return self.name + " " + str(self.score)

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0


n = int(input())
players = []
for i in range(n):
    name, score = input().split()
    player = Player(name, int(score))
    players.append(player)

l = sorted(players, key=cmp_to_key(Player.comparator))
for i in players:
    print(i)
