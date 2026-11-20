import numpy as np
from sim.players import Player

def calc_win_probability(true_skill_1, true_skill_2):
    return 1 / (1 + 10**((true_skill_2-true_skill_1) / 400)) # takes two true skills and calculates the win probabilty of true skill 1 winning

def play_match(player_1, player_2, rng):
    player_1.add_games_played()
    player_2.add_games_played()

    player_1_chance = calc_win_probability(player_1.true_skill, player_2.true_skill)
    if player_1_chance > rng.random():
        return player_1,player_2
    else:
        return player_2, player_1

    # returns winner first then loser

if __name__ == "__main__":

    seed = 42
    counter = 0

    rng = np.random.default_rng(seed)
    player_a = Player(0,1600)
    player_b = Player(1,1400)

    for i in range(10000):
          winner,loser = play_match(player_a, player_b, rng)
          if winner is player_a:
           counter = counter + 1 # counts a's wins

    a_win_prediction = calc_win_probability(player_a.true_skill, player_b.true_skill) # calculates the probability of a winning based on its true skill
    a_win_rate = counter / 10000 # rate of a winning over 10k runs
     
    print(f"A's odds of winning each based on true skill: {a_win_prediction}")
    print(f"A's actual win rate over 10k runs: {a_win_rate}")

    print(f"A's games played: {player_a.games_played}")
    print(f"B's games played: {player_b.games_played}")