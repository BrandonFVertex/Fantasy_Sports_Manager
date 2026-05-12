# ================================
# main.py
# ================================
# You might run or change this file as you see fit to test out your Team class.
# You must fix bugs within the module.py file to fix the team class.

from module import Team

team = Team()

team.add_player("Mahomes", 25)
team.add_player("Kelce", 18)
team.add_player("Allen", 30)

print("Players:", team.players)

print("Total Points:", team.total_points())

print("Highest Scorer:", team.highest_scorer())

print("Average Points:", team.get_average_points())

print("Top Two Players:", team.get_top_two())

team.bench_player("Kelce")

print("After Bench:", team.players)