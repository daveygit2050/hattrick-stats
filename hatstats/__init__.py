from hatstats import load_csv
from hatstats import team

team_list = load_csv.load_teams()
team_chars = len(max(team_list, key=lambda team: len(team.name)).name)

print('\n*Average player salary (total players)*')
sorted_list = sorted(team_list, key=lambda team: team.avg_salary, reverse=True)
for team in sorted_list:
    print('```{0:{1}} - £{2:,.2f} ({3})```'.format(team.name, team_chars, team.avg_salary, team.player_count))

print('\n*Average player age*')
sorted_list = sorted(team_list, key=lambda team: (team.avg_age.years, team.avg_age.days), reverse=True)
for team in sorted_list:
    print('```{0:{1}} - {2} ({3})```'.format(team.name, team_chars, team.avg_age.years, team.avg_age.days))

print('')
