class Team:
    def __init__(self, name, salary, player_count):
        self.name = name
        self.salary = salary
        self.player_count = player_count
        self.avg_salary = salary / player_count
