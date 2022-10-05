from calendar import weekday, day_name

def most_frequent_days(year):
    days = [weekday(year, 1, 1), weekday(year, 12, 31)]
    return [day_name[i] for i in sorted(list(set(days)))]


"""
Найти наибольшое кол-во дней недели в году
"""
