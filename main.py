from functools import cmp_to_key


def unique_names(l1: list, l2: list) -> list:
    return sorted(set(l1 + l2))


def group_by_owners(files: dict) -> dict:
    owners = {}
    for i in files:
        if files[i] in owners:
            owners[files[i]].append(i)
        else:
            owners[files[i]] = [i]
    return owners


class LeagueTable:
    def __init__(self, players_name: list):
        self.players = {pl: {'ind': ind, 'count': 0, 'total': 0}
                        for ind, pl in enumerate(players_name, 1)}
        self.count_players = len(players_name)

    def record_result(self, name: str, score: int) -> None:
        if name in self.players:
            self.players[name]['count'] += 1
            self.players[name]['total'] += score
        else:
            self.count_players += 1
            self.players[name]['ind'] = self.count_players
            self.players[name]['count'] = 1
            self.players[name]['total'] = score

    def player_rank(self, rank: int) -> str:
        def my_cmp(a, b):
            a, b = self.players[a], self.players[b]
            diff = a['total'] - b['total']
            if diff != 0:
                return diff
            diff = b['count'] - a['count']
            if diff != 0:
                return diff
            return b['ind'] - a['ind']
        ranks = sorted(self.players, key=cmp_to_key(my_cmp), reverse=True)
        return ranks[rank - 1]
