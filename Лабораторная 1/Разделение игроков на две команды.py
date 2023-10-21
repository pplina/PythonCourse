list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

total_players = len(list_players)
mid = total_players // 2
team1 = list_players[:mid]
team2 = list_players[mid:]

print(team1)
print(team2)
