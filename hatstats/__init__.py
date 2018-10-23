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

print('\n*Max stadium attendance*')
sorted_list = sorted(team_list, key=lambda team: (team.max_attendance, team.stadium_capacity), reverse=True)
for team in sorted_list:
    percentage_attendance = float(team.max_attendance) * (100.0 / float(team.stadium_capacity))
    print('```{0:{1}} - {2:,}/{3:,} ({4:.0f}%)```'.format(team.name, team_chars, team.max_attendance, team.stadium_capacity, percentage_attendance))

print('')
