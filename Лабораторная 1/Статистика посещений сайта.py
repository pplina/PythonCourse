users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

statistics = {"Общее количество": len(users), "Уникальные посещения": 0}

unique_users = set(users)
statistics["Уникальные посещения"] = len(unique_users)
print(statistics)
