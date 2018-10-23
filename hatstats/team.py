class Team:
    def __init__(self, name, salary, player_count, avg_age, stadium_capacity, max_attendance):
        self.name = name
        self.salary = salary
        self.player_count = player_count
        self.avg_salary = salary / player_count
        self.avg_age = avg_age
        self.stadium_capacity = stadium_capacity
        self.max_attendance = max_attendance
