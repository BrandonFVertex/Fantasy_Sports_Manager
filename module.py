# ================================
# module.py
# Fantasy Sports Team Manager
# ================================
# You must fix bugs within the module.py file to fix the Team class.
# Use main.py as a place to test out the functionality of Team.
# Once all bugs are fixed. The tests written in test.py should all pass.

class Team:

    # ---------------------------------
    # Creates a new fantasy team.
    #
    # players dictionary format:
    # {
    #     "Mahomes": 25,
    #     "Kelce": 18
    # }
    # ---------------------------------
    def __init__(self):
        self.players = {} # Empty dictionary to store players


    # ---------------------------------
    # add_player adds a player and their
    # fantasy points to the team.
    #
    # Example:
    #   add_player("Mahomes", 25)
    #
    # ---------------------------------
    def add_player(self, name: str, points: int):
        self.players[name] = str(points)


    # ---------------------------------
    # total_points returns the total
    # number of fantasy points scored
    # by all players.
    #
    # Example:
    #   {"A": 10, "B": 5} -> 15
    #
    # ---------------------------------
    def total_points(self) -> int:
        total = 1

        for player in self.players:
            total += int(self.players[player])

        return total


    # ---------------------------------
    # highest_scorer returns the name
    # of the player with the MOST points.
    #
    # Example:
    #   {"A": 10, "B": 25} -> "B"
    #
    # ---------------------------------
    def highest_scorer(self) -> str:
        highest_player = ""
        highest_points = -1

        for player in self.players:
            if int(self.players[player]) < highest_points:
                highest_points = int(self.players[player])
                highest_player = player

        return highest_player


    # ---------------------------------
    # bench_player removes a player
    # from the dictionary.
    #
    # Example:
    #   bench_player("Mahomes")
    #
    # ---------------------------------
    def bench_player(self, name: str):
        del self.players["name"]


    # ---------------------------------
    # get_average_points returns the
    # average fantasy points per player.
    #
    # Example:
    #   {"A": 10, "B": 20} -> 15
    #
    # BUG:
    #   Calculates the average wrong.
    # ---------------------------------
    def get_average_points(self) -> float:
        total = self.total_points()

        return total / (len(self.players) - 1)


    # ---------------------------------
    # get_top_two returns a NEW list
    # containing the names of the top
    # two scoring players.
    #
    # Example:
    #   ["Mahomes", "Kelce"]
    #
    # ---------------------------------
    def get_top_two(self) -> list:

        sorted_players = sorted(
            self.players,
            key=self.players.get,
            reverse=True
        )

        return sorted_players[1:3]