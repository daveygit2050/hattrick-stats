from hatstats import load_csv
from hatstats import team

team_list = load_csv.load_teams()
sorted_list = sorted(team_list, key=lambda team: team.avg_salary, reverse=True)
print('*Average player salary (total players)*')
for team in sorted_list:
    print('```{} - £{:,.2f} ({})```'.format(team.name, team.avg_salary, team.player_count))
