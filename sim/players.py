import numpy as np

class Player:
    def __init__(self, player_id, true_skill, rating=1500): # rating is preset if not passed to mimic new account created
        self.player_id = player_id
        self.true_skill = true_skill
        self.rating = rating

        self.games_played = 0 # not set before as always starts at 0

    def __repr__(self): # print function of an object made from this class
        rounded_true_skill = round(self.true_skill,1)
        return f"Player id: {self.player_id}, true skill: {rounded_true_skill}, rating: {self.rating}, games: {self.games_played}"

    def add_games_played(self):
        self.games_played = self.games_played + 1

def generate_players(player_amount=1000, avg_true_skill=1500, true_skill_spread=300, seed=42):
    rng = np.random.default_rng(seed) # holds the random dice generator
    true_skills = rng.normal(avg_true_skill, true_skill_spread, player_amount) # creates array of true skills using these values from bell curve of length player amount with mean (loc) 1500 and stdev of true_skill_spread
    players_list = []

    for i in range(0,len(true_skills)):
        new_player = Player(i,true_skills[i]) # i so id starts at 0; no rating added so it simulates new player with default 1500
        players_list.append(new_player)

    return players_list

if __name__ == "__main__": # only if this is the current file being ran directly
    players_list = generate_players() # is assigned a list of player objects
    print(len(players_list))
    for i in range(len(players_list)):
        print(players_list[i].true_skill)

    print(all(player.rating == 1500 for player in players_list)) # just to see if all ratings start at 1500

    for player in players_list[:5]: # test to print first 5 players - goes with the repr
        print(player)