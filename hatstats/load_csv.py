import csv

from hatstats import team

def load_teams():
    team_list = []
    with open('stats.csv', 'r') as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=',', quotechar='\"')
        for csv_row in csv_data:
            team_list.append(team.Team(
                    name = csv_row['Team'],
                    salary = int(csv_row['Total Salary']),
                    player_count = int(csv_row['Players'])
                ))
    return team_list
