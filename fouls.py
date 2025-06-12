import pandas as pd

# Load dataset
football = pd.read_csv("football18-19.csv")

# Count fouls for home and away teams
homeFouls = football['HomeTeam'].value_counts().reset_index()
homeFouls.columns = ['Team', 'HF']  # Rename columns

awayFouls = football['AwayTeam'].value_counts().reset_index()
awayFouls.columns = ['Team', 'AF']  # Rename columns

# Merge both datasets on the team name
totalFouls = homeFouls.merge(awayFouls, on='Team', how='outer').fillna(0)

# Sum home and away fouls
totalFouls['TotalFouls'] = totalFouls['HF'] + totalFouls['AF']

# Find the team with the highest foul count
mostFoulsTeam = totalFouls.loc[totalFouls['TotalFouls'].idxmax()]

print(mostFoulsTeam)