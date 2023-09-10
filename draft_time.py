


# Reading in the first line
n_teams, m_rounds, n_players = input().split(' ')

team_preferences = []
mached = {} # Dictionary to keep track of mached and unmached players

# Reading in the ream preferences
for teams in range(int(n_teams)):
    line = input().split(' ')
    team_name, players_ranked = line[0], line[1:] # The team name and the players they prefer
    team_preferences.append(players_ranked) 
    mached[team_name] = [] # This is the dictionary where i will keep all the maches


player_preferences = {} # Dictionary to keep track of the players and their preferences so teams can be compared later
for players in range(int(n_players)):
	line = input().split(' ')
	player, teams_ranked = line[0], line[1:]
	player_preferences[player] = teams_ranked 




mached_players = [] # Players that have already been mached

while any(len(players) < int(m_rounds) for players in mached.values()):  # Keep iterating until all teams have m_rounds players or no more valid matches can be made

	for i, (team,v) in enumerate(mached.items()): # Looping over the dictionary of teams with their current mached players

		idx = 0 # This is an index tracker to track which player the team is currently proposing to

		while len(v) != int(m_rounds) and idx < len(team_preferences[i]): # While there are still players to macth for the team and still players in the preferences list

			player = team_preferences[i][idx] # Current player that the team is proposing to

			if player not in mached_players: # If the player is not mached, we add it and the team
				mached_players.append(player)
				mached[team].append(player)


			else:
				player_pref = player_preferences[player] # List of teams that the player wants to be on

				current_matched_team = [team for team, players in mached.items() if player in players][0] # This is the name of the team that the player is on currently

				if player_pref.index(team) < player_pref.index(current_matched_team): # If the player prefers the current iteration of the team rather than the one it's already on, we switch it
					mached[current_matched_team].remove(player)     
					# Add the player to the new team in the mached dictionary
					mached[team].append(player)


			idx += 1 # Increment the index


if any(len(players) < int(m_rounds) for players in mached.values()): # If there is not enough players for the round there is no stable solution
    print("Hello darkness my old friend!")
else:
    for team, player in mached.items():
        print(team + ' ' + ' '.join(player))

# Note: I had some help from generative ai to generate test cases, which made me realize that I was not using m_rounds to assign number of players, but simply 2 like in the provided example.

