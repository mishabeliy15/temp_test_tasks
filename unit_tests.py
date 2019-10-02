import unittest
from .main import unique_names, group_by_owners, LeagueTable


class Tests(unittest.TestCase):

    def test_unique_names(self):
        self.assertEqual(unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']),
                         ['Ava', 'Emma', 'Olivia', 'Sophia'])

    def test_group_by_owners(self):
        self.assertEqual(group_by_owners({'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}),
                         {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']})

    def test_LeagueTable(self):
        table = LeagueTable(['Mike', 'Chris', 'Arnold'])
        table.record_result('Mike', 2)
        table.record_result('Mike', 3)
        table.record_result('Arnold', 5)
        table.record_result('Chris', 5)
        self.assertEqual(table.player_rank(1), 'Chris')


if __name__ == '__main__':
    unittest.main()
