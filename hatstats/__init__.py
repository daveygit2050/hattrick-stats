from hatstats import load_csv
from hatstats import team

team_list = load_csv.load_teams()

print('\n*Average player salary (total players)*')
sorted_list = sorted(team_list, key=lambda team: team.avg_salary, reverse=True)
for team in sorted_list:
    print('```{} - £{:,.2f} ({})```'.format(team.name, team.avg_salary, team.player_count))

print('\n*Average player age*')
sorted_list = sorted(team_list, key=lambda team: (team.avg_age.years, team.avg_age.days), reverse=True)
for team in sorted_list:
    print('```{} - {} ({})```'.format(team.name, team.avg_age.years, team.avg_age.days))

print('')
