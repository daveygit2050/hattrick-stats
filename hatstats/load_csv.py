import csv

from hatstats.age import Age
from hatstats.team import Team

def load_teams():
    team_list = []
    with open('stats.csv', 'r') as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=',', quotechar='\"')
        for csv_row in csv_data:
            avg_age_array = csv_row['Average Age'].split("-")
            avg_age_object = Age(years = avg_age_array[0], days = avg_age_array[1])
            team_list.append(Team(
                    name = csv_row['Team'],
                    salary = int(csv_row['Total Salary']),
                    player_count = int(csv_row['Players']),
                    avg_age = avg_age_object
                ))
    return team_list
